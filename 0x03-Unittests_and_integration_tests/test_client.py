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
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, path, mock):
        """a test method that checks if the GithubOrgClient returns
        the correct value"""
        obj1 = GithubOrgClient(path)
        obj1.org()
        url = "https://api.github.com/orgs/{org}"
        mock.assert_called_once_with(url.format(org=path))
