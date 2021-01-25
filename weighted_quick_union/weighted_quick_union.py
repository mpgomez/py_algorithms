class WeightedQuickUnion_V1:
    def __init__(self, n_points):
        # Initialize to be in different components (not connected)
        self.ids = [x for x in range(1, n_points)]
        self.num_elements = n_points

    def find_root(self, id, weight = 0):
        current_id = id
        if current_id == self.ids[current_id]:
            return current_id, weight
        else:
            return self.find_root(self.ids[current_id], weight + 1)

    def find_root_no_weight(self, id):
        root, _ = self.find_root(id)
        return root

    def union(self, a, b):
        """
        Connects two elements a and b.
        It will do so by pointing the root of a to the root of b
        :param a: first element to connect
        :param b: second element to connect
        :return:
        """
        root_a, weight_a = self.find_root(a)
        root_b, weight_b = self.find_root(b)
        if weight_a > weight_b:
            self.ids[root_b] = root_a
        else:
            self.ids[root_a] = root_b

    def connected(self, a, b):
        return self.find_root_no_weight(a) == self.find_root_no_weight(b)

class WeightedQuickUnion:
    def __init__(self, n_points):
        # Initialize to be in different components (not connected)
        self.ids = [x for x in range(0, n_points)]
        self.weight = [1 for x in range(0, n_points)]
        self.num_elements = n_points

    def find_root(self, id, weight = 0):
        current_id = id
        if current_id == self.ids[current_id]:
            return current_id, weight
        else:
            return self.find_root(self.ids[current_id], weight + 1)

    def find_root_no_weight(self, id):
        root, _ = self.find_root(id)
        return root

    def union(self, a, b):
        """
        Connects two elements a and b.
        It will do so by pointing the root of a to the root of b
        :param a: first element to connect
        :param b: second element to connect
        :return:
        """
        root_a = self.find_root_no_weight(a)
        root_b = self.find_root_no_weight(b)
        if self.weight[root_a] > self.weight[root_b]:
            self.ids[root_b] = root_a
            self.weight[root_a] += self.weight[root_b]
        else:
            self.ids[root_a] = root_b
            self.weight[root_b] += self.weight[root_a]

    def connected(self, a, b):
        return self.find_root_no_weight(a) == self.find_root_no_weight(b)
