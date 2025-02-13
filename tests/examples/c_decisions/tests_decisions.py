import unittest

from src.examples.c_decisions.decisions import is_consonant, is_even, is_number_in_range, is_vowel, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):

        self.assertEqual(False and False,False)
        self.assertEqual(True and False,False)
        self.assertEqual(False and True,False)
        self.assertEqual(True and True,True)

    def test_or_truth_table(self):
        self.assertEqual(False or False, False)
        self.assertEqual(True or False,True)
        self.assertEqual(False or True, True)
        self.assertEqual(True or True, True)

    def test_not_truth_table(self):
        self.assertEqual(not False, True)
        self.assertEqual(not True, False)

    def test_compare_numbers_equality(self):
        self.assertEqual((10,5), False)
        self.assertEqual((10,10), True)

    def test_is_number_in_range(self):
        self.assertEqual(is_number_in_range(1, 15, 5), True)
        self.assertEqual(is_number_in_range(1, 15, 16), False)

    def test_is_vowel(self):
        self.assertEqual(is_vowel('a'),True)
        self.assertEqual(is_vowel('e'), True)
        self.assertEqual(is_vowel('i'), True)

    def test_is_consonant(self):
        self.assertEqual(is_consonant('b'), True)
        self.assertEqual(is_consonant('a'), False)

    def test_is_even(self):
        self.assertEqual(is_even(3), False)#not even
        self.assertEqual(is_even(2), True)#even





