import unittest

from aids.sorting_and_searching.binary_search import binary_search_recursive, binary_search_iterative

class BinarySearchTestCase(unittest.TestCase):
    '''
    Unit tests for binary search

    '''

    def setUp(self):
        self.example_1 = [2, 3, 4, 10, 40]
        self.example_2 = []

    def test_binary_search_recursive(self):
        result = binary_search_recursive(self.example_1, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result,3)

    def test_binary_search_iterative(self):
        result = binary_search_iterative(self.example_1, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result,3)

    def test_binary_search_recursive_empty(self):
        result = binary_search_recursive(self.example_2, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result, None)

    def test_binary_search_iterative_empty(self):
        result = binary_search_iterative(self.example_2, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result, None)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
