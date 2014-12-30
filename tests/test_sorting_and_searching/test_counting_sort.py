import unittest

from aids.sorting_and_searching.counting_sort import counting_sort

class CountingSortTestCase(unittest.TestCase):
    '''
    Unit tests for counting sort

    '''

    def setUp(self):
        self.example = [4,3,2,1,4,3,2,4,3,4]

    def test_selection_sort(self):
        self.assertEqual(counting_sort(self.example), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
