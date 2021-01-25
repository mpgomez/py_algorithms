import unittest

from weighted_quick_union import WeightedQuickUnion


class QuickFindTests(unittest.TestCase):

    def test_basic(self):
        qu = WeightedQuickUnion(10)
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
        qu.union(4,3)
        self.assertTrue(qu.connected(4, 1))
        self.assertFalse(qu.connected(0, 5))

    def test_weight(self):
        qu = WeightedQuickUnion(10)
        # Now, connect some
        qu.union(0, 1)
        self.assertEquals(qu.weight[0], 1)
        self.assertEquals(qu.weight[1], 2)
        qu.union(0, 2)
        self.assertEquals(qu.weight[0], 1)
        self.assertEquals(qu.weight[2], 1)
        self.assertEquals(qu.weight[1], 3)



