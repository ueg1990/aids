import unittest

from aids.linked_list.linked_list import LinkedList

class LinkedListTestCase(unittest.TestCase):
    '''
    Unit tests for the Linked List data structure

    '''
 
    def setUp(self):
		self.test_linked_list = LinkedList()

	def test_stack_initialization(self):
		self.assertTrue(isinstance(self.test_linked_list, LinkedList))

	def test_linked_list_is_empty(self):
		self.assertTrue(self.test_linked_list.is_empty())

	def test_linked_list_size(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.assertEqual(self.test_linked_list.size(), 2)

	def test_linked_list_add(self):
		self.test_linked_list.add(1)
		self.assertEqual(self.test_linked_list.head.get_data(), 1)

	def test_linked_list_search(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.test_linked_list.add(3)
		self.test_linked_list.add(4)
		self.assertTrue(self.test_linked_list.search(3))

	def test_linked_list_search_false(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.test_linked_list.add(3)
		self.test_linked_list.add(4)
		self.assertFalse(self.test_linked_list.search(11))

	def test_linked_list_search_empty(self):
		self.assertFalse(self.test_linked_list.search(3))

	def test_linked_list_remove_first(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.test_linked_list.add(3)
		self.test_linked_list.add(4)
		self.test_linked_list.remove(1)
		self.assertEqual(self.test_linked_list.head.get_data(), 2)

	def test_linked_list_remove_last(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.test_linked_list.add(3)
		self.test_linked_list.add(4)
		self.test_linked_list.remove(4)
		self.assertEqual(self.test_linked_list.size(), 3)

	def test_linked_list_remove(self):
		self.test_linked_list.add(1)
		self.test_linked_list.add(2)
		self.test_linked_list.add(3)
		self.test_linked_list.add(4)
		self.test_linked_list.remove(3)
		self.assertEqual(self.test_linked_list.size(), 3)

    def tearDown(self):
        pass