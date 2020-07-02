class QuickUnion:
    def __init__(self, n_points):
        # Initialize to be in different components (not connected)
        self.ids = [x for x in range(0, n_points)]
        self.num_elements = n_points

    def find_root(self, id):
        current_id = id
        if current_id == self.ids[current_id]:
            return current_id
        else:
            return self.find_root(self.ids[current_id])

    def union(self, a, b):
        """
        Connects two elements a and b.
        It will do so by pointing the root of a to the root of b
        :param a: first element to connect
        :param b: second element to connect
        :return:
        """
        self.ids[self.find_root(a)] = self.find_root(b)

    def connected(self, a, b):
        return self.find_root(a) == self.find_root(b)