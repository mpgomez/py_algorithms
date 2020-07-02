import unittest

from quick_find import QuickFind


class QuickFindTests(unittest.TestCase):

    def test_basic(self):
        qf = QuickFind(10)
        # Initially, no elements will be connected
        self.assertFalse(qf.connected(0, 1))
        self.assertFalse(qf.connected(4, 8))

        # Now, connect some
        qf.union(0, 1)
        qf.union(4, 8)
        qf.union(5, 2)
        self.assertTrue(qf.connected(0, 1))
        self.assertTrue(qf.connected(4, 8))
        self.assertTrue(qf.connected(5, 2))

        qf.union(0, 8)
        self.assertTrue(qf.connected(4, 1))
        self.assertFalse(qf.connected(0, 5))

