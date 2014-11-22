import unittest

from aids.sorting_and_searching.quicksort import quicksort

class QuicksortTestCase(unittest.TestCase):
    '''
    Unit tests for quicksort
    '''

    def setUp(self):
        self.example_1 = [18,5,3,1,19,6,0,7,4,2,5]

    def test_quicksort(self):
        quicksort(self.example_1)
        self.assertEqual(self.example_1,[0,1,2,3,4,5,5,6,7,18,19])
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
