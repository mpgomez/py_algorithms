from unittest import TestCase

from greed_is_good.greed_is_good import score
from range_extraction.range_extraction import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(solution([-6, -3, -2, -1, 0, 1, ]), '-6,-3-1')
        self.assertEqual(score([2, 3, 4, 6, 2]), 0)
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)

        self.assertEqual(score([5, 5, 5, 4, 5]), 550)
        self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
