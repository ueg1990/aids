import unittest

from aids.sorting_and_searching.bubble_sort import bubble_sort

class BubbleSortTestCase(unittest.TestCase):
    '''
    Unit tests for bubble sort

    '''

    def setUp(self):
        self.example_1 = [18,5,3,1,19,6,0,7,4,2,5]

    def test_bubble_sort(self):
        bubble_sort(self.example_1)
        self.assertEqual(self.example_1,[0,1,2,3,4,5,5,6,7,18,19])


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
