class BST:
    """
    Class that implements a Binary Search Tree.
    A BST us a binary tree in symmetric order. It is either
    * Empty
    * Two disjoint binary trees (left and right)

    Symmetric order: every node key is:
    * Larger than all the keys in the left subtree
    * Smaller than all keys in right subtree
    """

    def __init__(self):
        self.root = None

    def get(self, key):
        """
        Function that will search for a key in a tree.
        :param key: key we are looking for
        :return: BSTNode containing the key we are looking for.
                None otherwise.
        """
        node = self.root
        while node is not None:
            if node.key == key:
                return node
            elif key < node.key:
                node = node.left
            else:  # key > node
                node = node.right
        return None

    def put(self, key, value):
        """
        Adds a new key-value pair. If:
        * The key already exists, the value will be updated
        * It is a new key: the value will be added
        See __insert
        :param key: new key or key to update
        :param value: value associated with the key
        :return: nothing
        """
        if self.root is None:
            self.root = BSTNode(key, value)
        node = self.get(key)
        if node is not None:
            node.value = value
        else:
            self.__insert(self.root, key, value)

    def max(self):
        """
        Finds the maximum node (the node with the biggest key)
        :return: BSTNode with the maximum key
        """
        node = self.root
        while node is not None:
            node = node.right
        return node

    def min(self):
        """
         Finds the minimum node (the node with the smallest key)
         :return: BSTNode with the minimum key
         """
        return self.min_subtree(self.root)

    def min_subtree(self, node):
        """
         Finds the minimum node (the node with the smallest key) in the subtree hanging from node
         :param node: subreee where we want to find the minimum
         :return: BSTNode with the minimum key

         NOTE: can be converted to static and taken out of the class. Leaving it here for clarity as this is just
         for learning
         """
        while node is not None:
            node = node.left
        return node

    def floor(self, key):
        """
        Returns the closest element that is less or equal than key
        :param key:
        :return:
        """
        return self.__floor_recursive(self.root, key)

    def rank(self, key):
        """
        Returns number of keys smaller or equal to K
        :param key:
        :return: number of keys smaller or equal to k.
        """
        rank_node = self.floor(key)
        if rank_node is None:
            return 0
        else:
            return rank_node.size()

    def size(self):
        if self.root is None:
            return 0
        return self.root.size()

    def inorder(self, node, queue_list):
        """
        Inorder traversal of the tree. Will yield the elements in natural ascending order
        :param node: node to start from
        :param queue_list: queue to append the next node. GETS MODIFIED.
        :return:
        """
        if node is None:
            return
        self.inorder(node.left, queue_list)
        queue_list.append(node)
        self.inorder(node.right, queue_list)

    def del_min(self):
        if self.root is not None:
            self.root = self.__del_min_recursive(self.root)

    def __iter__(self, node=-1):
        my_list = []
        self.inorder(self.root, my_list)
        for item in my_list:
            yield item

    def delete(self, key):
        if self.root is None:
            return self.root
        self.root = self.__delete_recursive(self.root, key)

    def __floor_recursive(self, node, key):
        if node is None:
            return node
        if node.key == key:
            return node
        if key < node.key:
            return self.__floor_recursive(node.left, key)

        r_node = self.__floor_recursive(node.right, key)
        if r_node is not None:
            return r_node
        else:
            return node

    def __insert(self, node, key, value):
        """
        Where the magic happens. It is a bit tricky recursion, as we return a link to the node higher up.
        !!! You need to check that the node doesnt exist beforehand.
        Possible improvement would be to update the value here if the key exists (trivial)
        :param node: node where we want to hang the new "key,value" node.
        :param key: key to insert
        :param value: value to assoiate with the key
        :return: either the new node, or the updated hanging node.
        """
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:  # node < key
            node.right = self.__insert(node.right, key, value)
        # Addition!! - needed to maintain count
        node.recount()
        return node

    def __del_min_recursive(self, node):
        """
        To delete, we need to:
        * Keep going left until we find a null left link
        * Replace that node by its right link
        * Update counts of all the subtree
        We use the same recursive method of updating uper node links that we used in insertion
        :param node: subtree where we want to delete the minimum
        :return: the same node with the updated subtree
        """
        if node.left is None:
            return node.right
        node.left = self.__del_min_recursive(node.left)
        node.recount()
        return node

    def __delete_recursive(self, node, key):
        if node is None:
            return node
        # This is a search, but recursive, because we need the parent links and counts to be updated when we come back up
        if key < node.key:
            node.left = self.__delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.__delete_recursive(node.right, key)
        else:  # We found the node with key
            # If one of the children is None, we just update
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            # If there are more children, we need to replace the successor. That means, copy the successor, then delete
            # the successor from the tree, and replace the node we actually wanted to delete with the successor.
            # So we copy the current node
            original = node
            # We look for the successor: minimum key that is still greater than original. That is, the minimum in the right
            # subtree
            node = self.min(original.right)
            # we delete that right minimum, and make this new node point to the subtree from the original tree,
            # but without the minimum
            node.right = self.__del_min_recursive(original.right)
            # now we make the left subtree point to the same as the original
            node.left = original.left
        node.recount()
        return node


class BSTNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.left = parent
        self.count = 1
        self.recount()

    def recount(self):
        """
        Updates the size of a subtree.
        Very useful for recursive methods in the BST tree.
        """
        self.count = 1
        if self.left is not None:
            self.count += self.left.count
        if self.right is not None:
            self.count += self.right.count

    def size(self):
        return self.count
