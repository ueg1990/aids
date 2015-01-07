import unittest

from aids.strings.reverse_string.py import *

class ReverseStringTestCase(unittest.TestCase):
    '''
    Unit tests for reverse strings

    '''

    def setUp(self):
        self.example = "Pythonista"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
