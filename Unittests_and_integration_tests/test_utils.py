#!/usr/bin/env python3
import unittest
from unittest import mock
from functools import wraps

# Memoize decorator definition


def memoize(fn):
    """Memoizes the result of the function to avoid re-execution."""
    cache_name = f"_{fn.__name__}_cache"

    @wraps(fn)
    def wrapper(self):
        if not hasattr(self, cache_name):
            result = fn(self)
            setattr(self, cache_name, result)
        return getattr(self, cache_name)

    return wrapper


class TestMemoize(unittest.TestCase):
    """Test class to verify the memoize decorator functionality."""

    def test_memoize(self):
        """Test the memoization behavior of the decorator."""
        # Define the class inside the test method
        class TestClass:
            def a_method(self):
                """Simple method that returns 42."""
                return 42

            @memoize
            def a_property(self):
                """Property that calls a_method."""
                return self.a_method()

        # Create an instance of the class and mock a_method
        test_instance = TestClass()

        with mock.patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42

            # First call - should call a_method and return 42
            result1 = test_instance.a_property()
            self.assertEqual(result1, 42)
            mock_method.assert_called_once()

            # Second call - should return 42 but not call a_method again
            result2 = test_instance.a_property()
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()  # Still only called once


if __name__ == '__main__':
    unittest.main()
