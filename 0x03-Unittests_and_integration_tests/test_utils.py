#!/usr/bin/env python3
"""
Parametrize a unit test
"""
import unittest
import utils
from unittest.mock import patch
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict
)
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittest that tests the method utils.access_nested_map
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: int) -> Any:
        """
        test method to test if a functions returns the desired output
        """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")]
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> Any:
        """
        a test method that checks if KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    a class test that checks if a method returns the expected result
    """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> Dict:
        """
        a test method that checks if utils.get_json returns the expected
        result
        """
        with patch('utils.get_json') as mock_get:
            mock_get.return_value = test_payload
            res = utils.get_json(test_url)
            self.assertEqual(res, test_payload)
