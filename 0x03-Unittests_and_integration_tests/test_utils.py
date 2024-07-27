#!/usr/bin/env python3
'''test for access_nested_map'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Any
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    '''test class  for access_nested_map method'''

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        '''checkes for each parameterized input the output is correct'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence) -> None:
        '''testing exception when their is no mapping but key exists'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''''''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_request):
        '''
            testing get_json that returns a json by requesting to the
            url passed as an argument
        '''
        moke_response = MagicMock()
        moke_response.json.return_value = test_payload
        mock_request.return_value = moke_response
        self.assertDictEqual(get_json(test_url), test_payload)
        mock_request.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
