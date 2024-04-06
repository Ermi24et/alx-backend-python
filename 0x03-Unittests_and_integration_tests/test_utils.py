#!/usr/bin/env python3
"""
Parametrize a unit test
"""
import unittest
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any
)
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittest that tests the method utils.access_nested_map
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b":2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: int) -> Any:
        """
        test method to test if a functions returns the desired output
        """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)
