import unittest

from swap import swap


class SwapTest(unittest.TestCase):

    def test_swap_int(self):
        one = 1
        two = 2
        a = one
        b = two
        self.assertEqual(a, one)
        self.assertEqual(b, two)
        a, b = swap(a, b)
        self.assertEqual(a, two)
        self.assertEqual(b, one)

    @unittest.expectedFailure
    def test_swap_strings(self):
        one = "one"
        two = "two"
        a = one
        b = two
        self.assertEqual(a, one)
        self.assertEqual(b, two)
        a, b = swap(a, b)
        self.assertEqual(a, two)
        self.assertEqual(b, one)
