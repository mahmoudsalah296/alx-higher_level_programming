#!/usr/bin/python3
"""
max integer using unit test
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unit test class for max_integer function
    """

    def test_max_integer(self):
        """test max_integer function"""

        result = max_integer([0, 1])
        self.assertEqual(result, 1)

        result = max_integer([-1, 1])
        self.assertEqual(result, 1)

        result = max_integer([2, 1])
        self.assertEqual(result, 2)

        result = max_integer([1, 1])
        self.assertEqual(result, 1)

        result = max_integer([5])
        self.assertEqual(result, 5)

        result = max_integer([5, 5, 5])
        self.assertEqual(result, 5)

        result = max_integer([5.3, 5.2, 5.1])
        self.assertEqual(result, 5.3)

        result = max_integer([5.3, 5, 5.1])
        self.assertEqual(result, 5.3)

        result = max_integer([-5.3, -5.2, -5.1])
        self.assertEqual(result, -5.1)

        result = max_integer([1, -1])
        self.assertEqual(result, 1)

        result = max_integer([])
        self.assertIsNone(result)

        result = max_integer()
        self.assertIsNone(result)

        result = max_integer("mahmoud")
        self.assertEqual(result, "u")

        result = max_integer("")
        self.assertIsNone(result)

        result = max_integer(["mahmoud", "ahmed", "yasser"])
        self.assertEqual(result, "yasser")


if __name__ == '__main__':
    unittest.main()
