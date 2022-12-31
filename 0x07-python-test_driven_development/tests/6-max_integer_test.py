#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This module contains test functions that runs tests
    on the corresponding function with several test case
    scenarios.
    """
    
    def test_max_integer(self):
        """
        This test function asserts that all these test cases
        for equality using the 'max_integer function' holds.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([4, 6, 2, 10, 8]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(list((4, 10, 6, 8, 2))), 10)
        self.assertEqual(max_integer([4.0, 6.0, 2.0, 10.0, 8.0]), 10)
        self.assertEqual(max_integer([4, 6.89, 2.65, 10, 8.43]), 10)
        self.assertEqual(max_integer([0.25, 0.5, 0.75, True]), 1)
        self.assertEqual(max_integer([False, True]), 1)

        with self.assertRaises(TypeError):
            max_integer([4, 6, 2, 10, 8, "alpha"])
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer(True)
        with self.assertRaises(TypeError):
            max_integer(False)
        with self.assertRaises(TypeError):
            max_integer(2)
        with self.assertRaises(KeyError):
            max_integer({"a": 1, "b": 2, "c": 3, "d": 4})
    
if __name__ == "__main__":
    unittest.main()
