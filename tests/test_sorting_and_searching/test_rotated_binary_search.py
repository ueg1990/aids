import unittest

from aids.sorting_and_searching.rotated_binary_search import rotated_binary_search

class RotatedBinarySearchTestCase(unittest.TestCase):
    '''
    Unit tests for rotated binary search

    '''

    def setUp(self):
        pass

    def test_rotated_binary_search_second_half(self):
        self.assertEqual(rotated_binary_search([7,8,1,2,3,4,5], 4), 5)

    def test_rotated_binary_search_first_half(self):
        self.assertEqual(rotated_binary_search([7,8,1,2,3,5], 8), 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
