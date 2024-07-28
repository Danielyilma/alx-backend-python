#!/usr/bin/env python3
'''test module for GithubOrgClient class'''
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''unit test for GithubOrgClient class'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: Mock) -> None:
        '''tests the org method'''
        pay_load = {"status_code": 200}
        mock_get_json.return_value = pay_load
        instance = GithubOrgClient(org)
        self.assertDictEqual(instance.org, pay_load)
        self.assertDictEqual(instance.org, pay_load)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        '''test _public_repos_url property'''
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "www.example.com"}
            self.assertEqual(
                GithubOrgClient("abc")._public_repos_url,
                "www.example.com"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        '''test public repos'''

        public_url = "www.github.com"
        mock_get_json.return_value = [
            {
                "name": {"url": "www.github.com"},
                "license": {
                    "licence given by": "MIT license",
                    "key": "MIT123"
                }
            }
        ]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_pub_repo_url:
            mock_pub_repo_url.return_value = public_url
            instance = GithubOrgClient("abc")
            self.assertListEqual(
                instance.public_repos(),
                [{"url": public_url}]
            )
            self.assertListEqual(
                instance.public_repos(),
                [{"url": public_url}]
            )
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self, repo, license_key, expected):
        '''test haslicense static method'''
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''integration testing GithubOrgClient'''

    @classmethod
    def setUpClass(cls):
        '''setting up a patcher that return a mock object'''
        cls.get_patcher = patch("requests.get")
        cls.mock = cls.get_patcher.start()

        def side_effect(url):
            '''used to return  correct fixture for different value'''
            if url == "https://api.github.com/orgs/abc":
                mock_response = Mock()
                mock_response.json.return_value = cls.org_payload
                return mock_response
            elif url == "https://api.github.com/orgs/google/repos":
                mock_response = Mock()
                mock_response.json.return_value = cls.repos_payload
                return mock_response
        cls.mock.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        '''stops the patcher'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''test GithubOrgClient.public_repos'''
        self.assertListEqual(
            GithubOrgClient("abc").public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        '''test public_repos_with_license with license argument'''
        self.assertListEqual(
            GithubOrgClient("abc").public_repos("apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
