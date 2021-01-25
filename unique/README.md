Determine if a string has all unique characters

import unittest
from unique import is_unique

class TestIsUnique(unittest.TestCase):
	def test_is_unique(self):
		self.assertTrue(is_unique(“abcd”)
		self.assertTrue(is_unique(“abcdABCD”)
self.assertFalse(is_unique(“abcddABCD”)


def is_unique(string):
“””
Function that verifies if all the characters in a string are unique. It is case sensitive, meaning “A” and “a” are considered different characters

:param string: string to verify for uniqueness.

:return True: if it doesn’t have any duplicate characters
	False: otherwise
“””
	string_set = Set(list(string))
	if len(string_set) == len(string):
		return True
	else:
		return False