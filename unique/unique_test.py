import unittest
from unique import is_unique

class TestIsUnique(unittest.TestCase):
    def test_is_unique(self):
        self.assertTrue(is_unique("abcd"))
        self.assertTrue(is_unique("abcdABCD"))
        self.assertFalse(is_unique("abcddABCD"))


