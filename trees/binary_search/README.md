# Binary Search tree
A BST us a binary tree in symmetric order. It is either
* Empty
* Two disjoint binary trees (left and right)

Symmetric order: every node key is:
* Larger than all the keys in the left subtree
* Smaller than all keys in right subtree
This is different from heaps, where we had a node bigger than all children. Here, a node is between the value of its children

####Tree shape
The shape depends on the order in which the keys are added. The best case, it is balanced. The worst, it’s depth is N. Typically, it is somewhere in the middle.
With random keys, it is usually ~twice as deep as a balanced tree. It works similar to the quicksort pivoting.
## Implementation
A BST is a reference to a root node.
```python
class BST:
    def __init__(self):
        self. root = None
        self.size = 0

class BSTNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.left = parent
```


In our tree we will also need:
put
get
floor(k) bigger key in tree that is smaller or equal than K
delete
make it iterable

### Addition
In order to facilitate other applications, there is a "count" attribute in the node, that will count
how many nodes hang from it.
The size of a tree will just be the count of the root.

### Problematic
We will start having problems when we start doing deletions. If we start inserting/deleting, the tree becomes
more and more unbalances, and instead of logN efficiency, we get square root of N.
Next step would be to look into balanced trees and red black.