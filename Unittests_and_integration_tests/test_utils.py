#!/usr/bin/env python3
""" A Function that tests the utils.py file."""
import unittest
from parameterized import parameterized
from utils import access_nested_map  

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
