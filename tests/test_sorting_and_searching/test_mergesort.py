import unittest

from aids.sorting_and_searching.mergesort import mergesort, merge

class MergesortTestCase(unittest.TestCase):
    '''
    Unit tests for mergesort
    '''

    def setUp(self):
        self.example_1 = [18,5,3,1,19,6,0,7,4,2,5]
        self.example_2 = [2,4,6,8,10]
        self.example_3 = [3,5,7,9]

    def test_mergesort(self):
        result = mergesort(self.example_1)
        self.assertEqual(result,[0,1,2,3,4,5,5,6,7,18,19])
        
    def test_merge(self):
        result = merge(self.example_2, self.example_3)
        self.assertEqual(result,[2,3,4,5,6,7,8,9,10])
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
