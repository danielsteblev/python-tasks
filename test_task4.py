from task4 import *
import unittest

class TestReverseString(unittest.TestCase):

    def test_reverse_area(self):
        self.assertEqual(reverse_string("а"),
                         "а")


