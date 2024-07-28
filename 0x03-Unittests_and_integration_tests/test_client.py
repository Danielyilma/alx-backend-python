#!/usr/bin/env python3
'''test module for GithubOrgClient class'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
