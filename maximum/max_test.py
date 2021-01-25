import unittest
from maximum.max import max_number

class TestMaxNumber(unittest.TestCase):
    def test_max_number_int(self):
        self.assertEqual(max_number(1, 3), 3)
        self.assertEqual(max_number(-1, -2), -1)
        self.assertEqual(max_number(-1, -1), 0)
