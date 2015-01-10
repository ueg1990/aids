import unittest

from aids.strings.reverse_string import *

class ReverseStringTestCase(unittest.TestCase):
    '''
    Unit tests for reverse strings

    '''

    def setUp(self):
        self.example = "Pythonista"

    def test_reverse_string_pythonic(self):
    	self.assertEqual(reverse_string_pythonic(self.example), "atsinohtyP")

    def test_reverse_string_iterative(self):
    	self.assertEqual(reverse_string_iterative(self.example), "atsinohtyP")

    def test_reverse_string_recursive(self):
    	self.assertEqual(reverse_string_recursive(self.example), "atsinohtyP")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
