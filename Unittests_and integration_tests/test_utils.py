import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # First test case: Simple key-value
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Second test case: Nested dictionary
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Third test case: Deeper key path
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
