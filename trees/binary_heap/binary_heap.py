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
        if self.__len() == 0:
            self.bh.append(item)
        self.bh.append(item)
        self.__swim(self.__len() - 1)

    def pop(self):
        max_item = self.bh[1]
        self.__exchange(1, self.__len() - 1)
        self.bh.pop()
        self.__sink(1)
        return max_item

    def max(self):
        return self.bh[1]

    def size(self):
        # One less, as we ignore the first item
        if self.__len() == 0:
            return 0
        return self.__len() - 1

    def __len(self):
        return len(self.bh)

    def __sink(self, position):
        while position*2 < self.__len() and self.bh[position] < self.bh[position * 2]:
            self.__exchange(position, position * 2)
            position = position*2

    def __swim(self, position):
        while int(position/2) >= 1 and self.bh[position] > self.bh[int(position/2)]:
            self.__exchange(position, int(position / 2))
            position = int(position/2)

    def __exchange(self, pos1, pos2):
        aux = self.bh[pos1]
        self.bh[pos1] = self.bh[pos2]
        self.bh[pos2] = aux
