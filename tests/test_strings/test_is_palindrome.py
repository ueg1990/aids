import unittest

from aids.strings.is_palindrome import is_palindrome

class IsPalindromeTestCase(unittest.TestCase):
    '''
    Unit tests for  is_palindrome

    '''

    def setUp(self):
        pass

    def test_is_palindrome_true_empty_string(self):
    	self.assertTrue(is_palindrome(''))

    def test_is_palindrome_true(self):
    	self.assertTrue(is_palindrome('madam'))

    def test_is_palindrome_false(self):
    	self.assertFalse(is_palindrome('xxyyzz'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
