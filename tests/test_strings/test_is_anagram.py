import unittest

from aids.strings.is_anagram import *

class IsAnagramTestCase(unittest.TestCase):
    '''
    Unit tests for  determine anagrams

    '''

    def setUp(self):
        pass

    def test_is_anagram_sort(self):
    	self.assertTrue(is_anagram_sort('listen', 'silent'))

    def test_is_anagram(self):
    	self.assertTrue(is_anagram('listen', 'silent'))

    def test_is_anagram_false(self):
    	self.assertFalse(is_anagram('cookie', 'kookie'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
