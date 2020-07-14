# Binary Heap
Heap implemented by using a complete, pseudo ordered binary tree.
* Keys in nodes
* Parent’s key not smaller than child key

Represented with an array (list):
* Indices start at 1
* Nodes in level order
* No links needed

## child’s key becomes larger than parent: insert
We just exchange the keys child and parent, moving up the tree until the parent is bigger or 
equal than the child. We call this "swim".
In order to insert a new item, we just append the item and swim to maintain order

## parent becomes bigger than one (or both) children: delete
We need to promote the biggest child, and keep doing this until the parent is always bigger than
the child. We call this "sink".
In order to delete the max item, we exchange the root and the last item, and sink it.

## Notes
This is an implementation intended for learning purposes only. It doesn't take into account exceptions
or different data types.