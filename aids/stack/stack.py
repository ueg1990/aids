'''
Implementation of Stack data structure

'''


class Stack(object):

    def __init__(self):
		'''
		Initialize stack

		'''
		self.items = []


    def is_empty(self):
		'''
		Return True if stack if empty else False
		
		'''
		return self.items == []


    def push(self, item):
		'''
		Push item to stack

		'''
		self.items.append(item)


    def pop(self):
		'''
		Pop item from stack

		'''
		return self.items.pop()


    def peek(self):
		'''
		Return value of item on top of stack

		'''
		return self.items[-1]

    
    def __len__(self):
		'''
		Return number of items in stack

		'''
		return len(self.items)
