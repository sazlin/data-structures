from linked_list import l_list, node


class EmptyQueueError(Exception):
    """An exception that is thrown when trying to dequeue an empty queue"""

    def __init__(self, message):
        Exception.__init__(self, message)


class _Queue_List(l_list):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.tail = None

    def insert_tail(self, val):
        if not self.size():
            self.insert(val)
        else:
            self.tail = self.tail.next = node(val, None)
            self.num_nodes += 1

    def insert(self, val):
        super(self.__class__, self).insert(val)
        if self.size() == 1:
            self.tail = self.head

    def remove(self, a_node):
        super(self.__class__, self).remove(a_node)
        if not self.size():
            self.tail = None

    def pop(self):
        retval = super(self.__class__, self).pop()
        if not self.size():
            self.tail = None
        return retval


class Queue(object):

    def __init__(self):
        """initialize the Queue"""
        self._ql = _Queue_List()

    def enqueue(self, val):
        """add an item to the Queue"""
        self._ql.insert_tail(val)

    def dequeue(self):
        """remove and return an item from the Queue"""
        if not self.size():
            raise EmptyQueueError("Queue is empty")
        return self._ql.pop()

    def size(self):
        """return the number of items in the queue"""
        return self._ql.size()
