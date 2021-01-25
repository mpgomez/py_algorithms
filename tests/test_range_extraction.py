from unittest import TestCase
from range_extraction.range_extraction import solution

class Test(TestCase):
    def test_solution(self):
        # self.assertEqual(solution([1]),'1')
        # self.assertEqual(solution([2,3]),'2,3')
        # self.assertEqual(solution([-1,1,2,3]),'-1,1-3')
        # self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        # self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
        #self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(solution([-6,-3,-2,-1,0,1,]), '-6,-3-1')
