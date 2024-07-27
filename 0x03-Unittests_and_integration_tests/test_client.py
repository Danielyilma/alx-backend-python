#!/usr/bin/env python3
''''''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''unit test for GithubOrgClient class'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        '''tests the org method'''
        pay_load = {"status_code": 200}
        mock_get_json.return_value = pay_load
        instance = GithubOrgClient(org)
        self.assertDictEqual(instance.org, pay_load)
        self.assertDictEqual(instance.org, pay_load)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
