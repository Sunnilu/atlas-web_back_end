#!/usr/bin/env python3
import unittest
from unittest import mock
from parameterized import parameterized
import utils

class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        # Create mock response object
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
       
        # Patch requests.get to return our mock response
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
           
            # Call the function being tested
            result = utils.get_json(test_url)
           
            # Verify get was called exactly once with correct URL
            mock_get.assert_called_once_with(test_url)
           
            # Verify returned payload matches expected
            self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
