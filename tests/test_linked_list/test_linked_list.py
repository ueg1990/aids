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

    def tearDown(self):
        pass