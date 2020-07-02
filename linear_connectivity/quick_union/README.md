# Second approach: quick union
A union-find algorithm is an algorithm that performs two useful operations on such a data structure: 
Connected: Determine which subset a particular element is in. This can be used for determining if two elements are in 
the same subset. 
Union: Join two subsets into a single subset.

Same data structure as quick find, different interpretation.
We need to be able to find the root, which is easy. To do a union, we just need to set the root of
 the two items in the union, we need to point the root of the second item to the root of the first item.
 
 The problem is that it can still be slow in the worst case scenario. With very tall trees, a search cam be O(n), as we
 will end up having to traverse all the tree.