
class FlattenedQuickUnion:
    def __init__(self, n_points):
        # Initialize to be in different components (not connected)
        self.ids = [x for x in range(0, n_points)]
        self.weight = [1 for x in range(0, n_points)]
        self.num_elements = n_points

    def find_root(self, id):
        # Here we make every node point to its grandparent. They will still be in the same tree, but we half the path.
        current_id = id
        while current_id != self.ids[current_id]:
            self.ids[current_id] = self.ids[self.ids[current_id]]
            current_id = self.ids[current_id]
        return current_id

    def union(self, a, b):
        """
        Connects two elements a and b.
        It will do so by pointing the root of a to the root of b
        :param a: first element to connect
        :param b: second element to connect
        :return:
        """
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if self.weight[root_a] > self.weight[root_b]:
            self.ids[root_b] = root_a
            self.weight[root_a] += self.weight[root_b]
        else:
            self.ids[root_a] = root_b
            self.weight[root_b] += self.weight[root_a]

    def connected(self, a, b):
        return self.find_root(a) == self.find_root(b)
