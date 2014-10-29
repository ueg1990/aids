import unittest

from sorting_and_searching import binary_search_recursive

class BinarySearchTestCase(unittest.TestCase):
    '''
    Unit tests for binary search

    '''

    def setUp(self):
        self.example_1 = [2, 3, 4, 10, 40]

    def test_binary_search_recursive(self):
        result = binary_search_recursive(self.example_1, 0, len(self.example_1) - 1, 10)
        self.assertEqual(result,3)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
