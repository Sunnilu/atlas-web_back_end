#!/usr/bin/env python3
import unittest
from unittest import mock
from parameterized import parameterized

class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        # Define the class inside the test method
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create instance and mock a_method
        test_instance = TestClass()
        with mock.patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42
           
            # First call - should call a_method and return 42
            result1 = test_instance.a_property()
            self.assertEqual(result1, 42)
            mock_method.assert_called_once()
           
            # Second call - should return 42 but not call a_method
            result2 = test_instance.a_property()
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()  # Still only called once

if __name__ == '__main__':
    unittest.main()
