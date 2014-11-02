import unittest

from aids.sorting_and_searching.selection_sort import selection_sort

class SelectionSortTestCase(unittest.TestCase):
    '''
    Unit tests for selection sort

    '''

    def setUp(self):
        self.example_1 = [2, 5, 4, 3, 1]

    def test_selection_sort(self):
        selection_sort(self.example_1)
        self.assertEqual(self.example_1,[1,2,3,4,5])


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
