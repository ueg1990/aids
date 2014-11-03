import unittest

from aids.sorting_and_searching.selection_sort import selection_sort

class SelectionSortTestCase(unittest.TestCase):
    '''
    Unit tests for selection sort

    '''

    def setUp(self):
        self.example_1 = [18,5,3,1,19,6,0,7,4,2,5]

    def test_selection_sort(self):
        selection_sort(self.example_1)
        self.assertEqual(self.example_1,[0,1,2,3,4,5,5,6,7,18,19])


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
