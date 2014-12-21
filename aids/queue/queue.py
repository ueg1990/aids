'''
Implementation of queue data structure

'''


class Queue(object):

    def __init__(self):
		'''
		Initialize queue

		'''
		self.items = []


    def is_empty(self):
		'''
		Return True if queue if empty else False
		
		'''
		return self.items == []


    def enqueue(self, item):
		'''
		Push item to queue

		'''
		self.items.insert(0,item)


    def dequeue(self):
		'''
		Pop item from queue

		'''
		return self.items.pop()

    
    def __len__(self):
		'''
		Return number of items in queue

		'''
		return len(self.items)