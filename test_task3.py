from task3 import *
import unittest


class TestSearchMaxSumOfSegments(unittest.TestCase):

    def test_reverse_area(self):
        test1 = [(6, 7), (4, 5), (2, 3)]
        test2 = [(2, 6), (10, 14), (5, 9), (7, 12), (1, 3), (13, 20)]
        test3 = [(1, 100), (200, 300)]
        test4 = [(2, 99)]
        test5 = [(12, 16), (1, 2), (30, 40), (11, 18), (5, 6), (14, 17)]
        sum1, segments1 = max_sum_of_segments(test1)
        sum2, segments2 = max_sum_of_segments(test2)
        sum3, segments3 = max_sum_of_segments(test3)
        sum4, segments4 = max_sum_of_segments(test4)
        sum5, segments5 = max_sum_of_segments(test5)

        self.assertEqual(sum1, 3)
        self.assertEqual(sum2, 16)
        self.assertEqual(sum3, 199)
        self.assertEqual(sum4, 97)
        self.assertEqual(sum5, 18)
