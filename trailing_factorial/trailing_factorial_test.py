import unittest
from trailing_factorial import factorial, count_trailing_zeros, count_trailing_zeros_factorial

class TrailingFactorialTest(unittest.TestCase):
    def test_small_factorial(self):
        self.assertEqual(count_trailing_zeros(factorial(5)), 1)
        self.assertEqual(count_trailing_zeros(factorial(10)), 2)
        self.assertEqual(count_trailing_zeros(factorial(15)), 3)

    def test_big_numbers(self):
        self.assertEqual(count_trailing_zeros_factorial(5), 1)
        self.assertEqual(count_trailing_zeros_factorial(10), 2)
        self.assertEqual(count_trailing_zeros_factorial(15), 3)

        self.assertEqual(count_trailing_zeros_factorial(18), 3)
        self.assertEqual(count_trailing_zeros_factorial(25), 6)
        self.assertEqual(count_trailing_zeros_factorial(40), 9)
