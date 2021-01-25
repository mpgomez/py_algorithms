import unittest
from collections import deque
from linked_list_duplicates.remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_positive(self):
        my_list = ["1", "2", "2", "3"]
        my_linked_list = deque(my_list)
        remove_duplicates(my_linked_list)
        self.assertIsInstance(my_linked_list, deque)
        self.assertEqual(deque( ["1", "2", "3"]), my_linked_list)