import unittest
'''
the file in /tests/homework/e_functions/tests_functions
has the test functions
'''
from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)
