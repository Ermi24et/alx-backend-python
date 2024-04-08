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
        ["https://api.github.com/orgs/", "google"],
        ["https://api.github.com/orgs/", "abc"]
    ])
    def test_org(self, test_url: str, path: str) -> Dict:
        """a test method that checks if the GithubOrgClient returns
        the correct value"""
        with patch.object(GithubOrgClient, 'org') as mock_org:
            mock_org.return_value = "success"
            obj1 = GithubOrgClient(test_url+path)
            res = obj1.org()
            self.assertEqual(res, "success")
