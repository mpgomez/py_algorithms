# Third approach: weighted quick union

Like quick union, but we are going to avoid long trees by weighting them. How do we do that? By, instead of linking 
two trees anyway we want in an union, we hang the SMALLER tree from the bigger one, by weighting it (counting the number
of elements when we find the root).
That means that, to connect two trees, we point the root of the smaller one to the root of the bigger one