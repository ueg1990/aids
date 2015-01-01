import unittest

from aids.sorting_and_searching.find_kth_smallest import find_kth_smallest

class FindKthSmallestTestCase(unittest.TestCase):
    '''
    Unit tests for find_kth_smallest
    '''

    def setUp(self):
        self.example_1 = [54,26,93,17,77,31,44,55,20]

    def test_find_kth_smallest(self):
        self.assertEqual(find_kth_smallest(self.example_1, 0, len(self.example_1) - 1, 3), 26)
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
