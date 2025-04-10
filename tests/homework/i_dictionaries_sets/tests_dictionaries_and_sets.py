#
import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix

class Test_Config(unittest.TestCase):
    def test_get_p_distance(self):
        self.assertEqual(get_p_distance(['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C']), 4)
    def test_get_p_distance_matrix(self):
        self.assertEqual(get_p_distance_matrix(['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']), [[0, 4, 1, 1],[4, 0, 4,3],[1, 4, 0, 2],[1, 3, 2, 0]])
