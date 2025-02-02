#!/usr/bin/env python3
""" A Function that test the utils.py file."""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import your utils module

class TestAccessNestedMap(unittest.TestCase):

    # ... (Existing test_access_nested_map method remains here) ...

@parameterized.expand([
    ({}, ("a",), "a"),
    ({"a": 1}, ("a", "b"), "b"),
    ({"a": {"b": 2}}, ("a", "b", "c"), "c"),
])
def test_access_nested_map_exception(self, nested_map, path, expected_msg):
    with self.assertRaises(KeyError) as context:
        access_nested_map(nested_map, path)
    self.assertEqual(context.exception.args[0], expected_msg)  # Use .args[0]
    
if __name__ == '__main__':
    unittest.main()