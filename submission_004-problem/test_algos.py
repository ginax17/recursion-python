import itertools
from itertools import combinations_with_replacement
import super_algos
import sys
import unittest

class TestFindMin(unittest.TestCase):
    def test_find_empty_elements(self):
        self.assertEqual(super_algos.find_min(''),-1)
    def test_find_non_integer_in_elements(self):
        self.assertEqual(super_algos.find_min(['a',1,'a']),-1)
    def test_test_for_correct_answer(self):
        self.assertEqual(super_algos.find_min([3,6,8,9,3,11]),3)
    def test_for_the_sum_of_list(self):
        self.assertEqual(super_algos.sum_all([3,6,8,9,3,11]),40)
    

if __name__ == "__main__":
    unittest.main()