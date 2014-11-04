import unittest

from aids.sorting_and_searching.binary_search import binary_search_recursive, binary_search_iterative

class BinarySearchTestCase(unittest.TestCase):
    '''
    Unit tests for binary search

    '''

    def setUp(self):
        self.example_1 = [2, 3, 4, 10, 40]
        self.example_2 = []
        self.example_3 = [4]
        self.example_4 = [2,5]

    def test_binary_search_recursive(self):
        result = binary_search_recursive(self.example_1, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result,3)

    def test_binary_search_iterative(self):
        result = binary_search_iterative(self.example_1, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result,3)

    def test_binary_search_recursive_empty(self):
        result = binary_search_recursive(self.example_2, 0, len(self.example_2) - 1, 10)
        self.assertEqual(result, None)

    def test_binary_search_iterative_empty(self):
        result = binary_search_iterative(self.example_2, 0, len(self.example_2) - 1, 10)
        self.assertEqual(result, None)

    def test_binary_search_recursive_single(self):
        result = binary_search_recursive(self.example_3, 0, len(self.example_3) - 1, 4)
        self.assertEqual(result, 0)

    def test_binary_search_iterative_single(self):
        result = binary_search_iterative(self.example_3, 0, len(self.example_3) - 1, 4)
        self.assertEqual(result, 0)

    def test_binary_search_recursive_double(self):
        result = binary_search_recursive(self.example_4, 0, len(self.example_4) - 1, 5)
        self.assertEqual(result, 1)

    def test_binary_search_iterative_double(self):
        result = binary_search_iterative(self.example_4, 0, len(self.example_4) - 1, 2)
        self.assertEqual(result, 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
