'''
Implement Queue data structure using two stacks

'''

from stack import Stack

class QueueUsingTwoStacks(object):
	def __init__(self):
		'''
		Initialize Queue

		'''
		self.stack1 = Stack()
		self.stack2 = Stack()

	def is_empty(self):
		'''
		Return True if queue if empty else False
		
		'''
		return self.stack1.is_empty() and self.stack2.is_empty()

	def enqueue(self,value):
		'''
		Enqueue item to queue

		'''
		self.stack1.push(value)

	def dequeue(self):
		'''
		Dequeue item from queue

		'''
		if not self.stack2.is_empty():
			return self.stack2.pop()
		while not self.stack1.is_empty():
			self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

	def __len__(self):
		'''
		Return number of items in Queue

		'''
		return len(self.stack1) + len(self.stack2)
