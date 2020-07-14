import unittest
from binary_heap import BinaryHeap

class TestBinaryTree(unittest.TestCase):
    def test_binary_heap_push(self):
        bh = BinaryHeap()
        self.assertEqual(bh.size(), 0)
        bh.push(1)
        bh.push(2)
        bh.push(3)
        self.assertEqual(bh.size(), 3)

    def test_binary_heap_pop(self):
        bh = BinaryHeap()
        bh.push(1)
        bh.push(3)
        bh.push(2)
        self.assertEqual(bh.pop(), 3)
        self.assertEqual(bh.size(), 2)
        self.assertEqual(bh.pop(), 2)
        self.assertEqual(bh.size(), 1)
        self.assertEqual(bh.pop(), 1)
        self.assertEqual(bh.size(), 0)
