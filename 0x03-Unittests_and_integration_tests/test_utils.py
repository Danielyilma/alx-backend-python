#!/usr/bin/env python3
'''test for access_nested_map'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, MagicMock, Mock


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
    def test_get_json(self, test_url: str, test_payload: Dict, mock_request: Mock) -> None:
        '''
            testing get_json that returns a json by requesting to the
            url passed as an argument
        '''
        moke_response = MagicMock()
        moke_response.json.return_value = test_payload
        mock_request.return_value = moke_response
        self.assertDictEqual(get_json(test_url), test_payload)
        mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''testing memoization to a class function called TestClass.a_method'''

    def test_memoize(self) -> None:
        '''tests if the a_method is called more than once'''
        class TestClass:
            '''used to demonstrate the usage of the memoization'''
            def a_method(self) -> int:
                '''class method'''
                return 42

            @memoize
            def a_property(self) -> any:
                '''class attribute'''
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42)\
                as mock_memoize:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_memoize.assert_called_once()


if __name__ == "__main__":
    unittest.main()
