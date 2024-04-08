#!/usr/bin/env python3
"""
parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    a test class for the GithubOrgClient class
    """

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, path, mock_org):
        """a method test for the GithubOrgClient.org"""
        obj1 = GithubOrgClient(path)
        obj1.org()
        mock_org.assert_called_once_with(f'https://api.github.com/orgs/{path}')

    def test_public_repos_url(self):
        """ a method to test _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_prop:
            payload = {"repos_url": "World"}
            mock_prop.return_value = payload
            obj1 = GithubOrgClient("some url")
            res = obj1._public_repos_url
            self.assertEqual(res, payload["repos_url"])
