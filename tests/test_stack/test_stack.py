import unittest

from aids.stack.stack import Stack

class StackTestCase(unittest.TestCase):
    '''
    Unit tests for the Stack data structure

    '''
 
    def setUp(self):
	pass

    def test_stack_initialization(self):
	test_stack = Stack()
	self.assertTrue(isinstance(test_stack, Stack))

    def test_stack_is_empty(self):
        test_stack = Stack()
	self.assertTrue(test_stack.is_empty())


    def tearDown(self):
        pass
