import unittest

from quick_union import QuickUnion


class QuickFindTests(unittest.TestCase):

    def test_basic(self):
        qu = QuickUnion(10)
        # Initially, no elements will be connected
        self.assertFalse(qu.connected(0, 1))
        self.assertFalse(qu.connected(4, 8))

        # Now, connect some
        qu.union(0, 1)
        qu.union(4, 8)
        qu.union(5, 2)
        self.assertTrue(qu.connected(0, 1))
        self.assertTrue(qu.connected(4, 8))
        self.assertTrue(qu.connected(5, 2))

        qu.union(0, 8)
        self.assertTrue(qu.connected(4, 1))
        self.assertFalse(qu.connected(0, 5))

