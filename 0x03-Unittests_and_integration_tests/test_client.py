#!/usr/bin/env python3
"""
parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch
from typing import (
    Dict
)
from client import (
    GithubOrgClient
)
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    a test class for the GithubOrgClient class
    """
    @parameterized.expand([
        ["google"],
        ["abc"]
    ])
    def test_org(self, path: str) -> Dict:
        """a test method that checks if the GithubOrgClient returns
        the correct value"""
        with patch('client.get_json') as mock_org:
            obj1 = GithubOrgClient(path)
            obj1.org()
            mock_org.assert_called_once_with(
                f"https://api.github.com/orgs/{path}"
                )
