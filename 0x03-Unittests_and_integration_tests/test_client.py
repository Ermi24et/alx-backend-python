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

    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, path: str, mock_json: MagicMock):
        """a test method that checks if the GithubOrgClient returns
        the correct value"""
        obj1 = GithubOrgClient(path)
        obj1.org()
        mock_json.assert_called_once_with(obj1.ORG_URL.format(org=path))

    def test_public_repos_url(self):
        """ a method to test _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_prop:
            payload = {"repos_url": "World"}
            mock_prop.return_value = payload
            obj1 = GithubOrgClient("some url")
            res = obj1._public_repos_url
            self.assertEqual(res, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mocked_json):
        """a test method to check if the output is as expected"""
        js_payload = [{"name": "somename"}, {"name": "somename1"}]
        mocked_json.return_value = js_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_prop:
            mock_prop.return_value = "some repo"
            obj1 = GithubOrgClient('some url').public_repos()
        self.assertEqual(['somename', 'somename1'], obj1)
        mocked_json.assert_called_once_with('some repo')
