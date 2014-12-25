import unittest

from aids.sorting_and_searching.max_subarray import max_subarray

class MaxSubArrayTestCase(unittest.TestCase):
    '''
    Unit tests for max_subarray

    '''

    def setUp(self):
        pass

    def test_all_positive(self):
        self.assertEqual(max_subarray([2,4,3,6,1,7]), (23, 0, 5))

    def test_all_negative(self):
        self.assertEqual(max_subarray([-2,-4,-3,-6,-1,-7]), (-1, 4, 4))

    def test_positive_and_negative(self):
        self.assertEqual(max_subarray([-2, 11, -4, 13, -5, 2]), (20, 1, 3))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
