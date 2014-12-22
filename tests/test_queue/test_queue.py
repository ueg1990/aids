import unittest

from aids.queue.queue import Queue

class QueueTestCase(unittest.TestCase):
    '''
    Unit tests for the Queue data structure

    '''
 
    def setUp(self):
		self.test_queue = Queue()

    def test_queue_initialization(self):
		self.assertTrue(isinstance(self.test_queue, Queue))

    def test_queue_is_empty(self):
        self.assertTrue(self.test_queue.is_empty())

    def test_queue_enqueue(self):
		self.test_queue.enqueue(1)
		self.assertEqual(len(self.test_queue), 1)
		
	def test_queue_dequeue(self):
		self.test_queue.enqueue(1)
		self.assertEqual(self.test_queue.dequeue(), 1)
		
	def test_queue_len(self):
		self.test_queue.enqueue(1)
		self.assertEqual(len(self.test_queue), 1)

    def tearDown(self):
        pass
