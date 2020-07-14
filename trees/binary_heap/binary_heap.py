class BinaryHeap:
    """
    Class that implements a binary heap (a heap that maintains the max element always on top) using a partially
    ordered complete binary tree, implemented using an array
    """
    def __init__(self):
        self.bh = []

    def push(self, item):
        # We need to ignore the first item so we don't mess up the calculations.
        # The first item gets inserted twice, and the 0 position, ignored.
        if self._len() == 0:
            self.bh.append(item)
        self.bh.append(item)
        self.swim(self._len() - 1)

    def pop(self):
        max = self.bh[1]
        self.exchange(1, self._len() - 1)
        self.bh.pop()
        self.sink(1)
        return max

    def _len(self):
        return len(self.bh)

    def size(self):
        # One less, as we ignore the first item
        if self._len() == 0:
            return 0
        return self._len() - 1

    def sink(self, position):
        while position*2 < self._len() and self.bh[position] < self.bh[position * 2]:
            self.exchange(position, position*2)
            position = position*2

    def swim(self, position):
        while int(position/2) >= 1 and self.bh[position] > self.bh[int(position/2)]:
            self.exchange(position, int(position/2))
            position = int(position/2)

    def exchange(self, pos1, pos2):
        aux = self.bh[pos1]
        self.bh[pos1] = self.bh[pos2]
        self.bh[pos2] = aux
