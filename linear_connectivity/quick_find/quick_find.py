# -*- coding: utf-8 -*-


class QuickFind:
    def __init__(self, n_points):
        # Initialize to be in different components (not connected)
        self.ids = [x for x in range(0, n_points)]
        self.num_elements = n_points

    def union(self, a, b):
        """
        Connects two elements a and b.
        Update all the elements with the same ID as a to have the same ID as b
        :param a: first element to connect
        :param b: second element to connect
        :return:
        """
        if self.ids[a] != self.ids[b]:
            old_id = self.ids[a]
            for i in range(0, self.num_elements):
                if self.ids[i] == old_id:
                    self.ids[i] = self.ids[b]

    def connected(self, a, b):
        return self.ids[a] == self.ids[b]