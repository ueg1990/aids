import unittest

from aids.stack.stack import Stack

class StackTestCase(unittest.TestCase):
    '''
    Unit tests for the Stack data structure

    '''
 
    def setUp(self):
		self.test_stack = Stack()

    def test_stack_initialization(self):
		self.assertTrue(isinstance(self.test_stack, Stack))

    def test_stack_is_empty(self):
        self.assertTrue(self.test_stack.is_empty())

	def test_stack_push(self):
		self.test_stack.push(1)
		self.assertEqual(len(self.test_stack), 1)
		
	def test_stack_peek(self):
		self.test_stack.push(1)
		self.assertEqual(self.test_stack.peek(), 1)
		
	def test_stack_pop(self):
		self.test_stack.push(1)
		self.assertEqual(self.test_stack.pop(), 1)
		
	def test_stack_size(self):
		self.test_stack.push(1)
		self.assertEqual(len(self.test_stack), 1)

    def tearDown(self):
        pass
