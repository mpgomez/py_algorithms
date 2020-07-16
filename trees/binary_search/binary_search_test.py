import unittest
from trees.binary_search.binary_search import BST

class TestBST(unittest.TestCase):
    def test_BST_Count(self):
        tree = BST()
        self.assertEqual(tree.size(), 0)
        tree.put(2, "2")
        self.assertEqual(tree.size(), 1)
        tree.put(1, "1")
        tree.put(3, "3")
        self.assertEqual(tree.size(), 3)

    def test_BST_inorder(self):
        tree = BST()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")
        key_list = [x.key for x in tree]
        self.assertEqual(tree.size(), 3)
        self.assertEqual([1, 2, 3], key_list)

    def test_BST_floor(self):
        tree = BST()
        tree.put(2, "2")
        tree.put(3, "3")
        tree.put(5, "5")
        self.assertEqual(tree.floor(4).key, 3)
        self.assertEqual(tree.floor(2).key, 2)
        self.assertEqual(tree.floor(5).key, 5)
        self.assertEqual(tree.floor(6).key, 5)
        self.assertIsNone(tree.floor(1))

    def test_BST_del_min(self):
        tree = BST()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")

        self.assertEqual(tree.size(), 3)
        tree.del_min()
        key_list = [x.key for x in tree]
        self.assertEqual(tree.size(), 2)
        self.assertEqual([2, 3], key_list)

    def test_BST_delete_root(self):
        tree = BST()
        tree.put(2, "2")

        self.assertEqual(tree.size(), 1)
        tree.delete(2)
        self.assertEqual(tree.size(), 0)

    def test_BST_delete(self):
        tree = BST()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")
        tree.put(5, "5")

        self.assertEqual(tree.size(), 4)
        tree.delete(3)
        key_list = [x.key for x in tree]
        self.assertEqual(tree.size(), 3)
        self.assertEqual([1, 2, 5], key_list)