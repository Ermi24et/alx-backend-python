#!/usr/bin/env python3
"""
parameterize and patch as decorators
"""
import unittest
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """a test method for GithubOrgClient.has_license"""
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """a test integration class"""

    @classmethod
    def setUpClass(cls):
        """mocks the request.get to return example payloads found in the fixtures"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """a method to stop the patcher"""
        cls.get_patcher.stop()