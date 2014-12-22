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

    def tearDown(self):
        pass
