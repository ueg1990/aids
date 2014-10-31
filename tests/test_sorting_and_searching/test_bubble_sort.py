import unittest

from aids.sorting_and_searching.bubble_sort import bubble_sort

class BubbleSortTestCase(unittest.TestCase):
    '''
    Unit tests for bubble sort

    '''

    def setUp(self):
        self.example_1 = [2, 5, 4, 3, 1]

    def test_bubble_sort(self):
        bubble_sort(self.example_1)
        self.assertEqual(self.example_1,[1,2,3,4,5])


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
