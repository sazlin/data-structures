class Node(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class DLinkedList(object):
    """A simple doubly linked list"""

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def insert(self, val):
        """insert val at head of the list"""
        if not self._size:
            self._tail = self._head = Node(val, None, None)
        else:
            self._head = Node(val, None, self._head)
            self._head.next.prev = self._head
        self._size += 1

    def append(self, val):
        """append val at the tail of the list"""
        if not self._size:
            self._tail = self._head = Node(val, None, None)
        else:
            self._tail = Node(val, self._tail, None)
            self._tail.prev.next = self._tail
        self._size += 1

    def pop(self):
        """pop the head of the list and return the head's value"""
        if self._head is None:
            return None
        else:
            retval = self._head.val
            self._head = self._head.next
            if self._head is not None:
                self._head.prev = None
            else:
                self._tail = None
            self._size -= 1
            return retval

    def shift(self):
        """remove the tail from the list and return the tail's value"""
        if self._tail is None:
            return None
        else:
            retval = self._tail.val
            self._tail = self._tail.prev
            if self._tail is not None:
                self._tail.next = None
            else:
                self._head = None
            self._size -= 1
            return retval

    def remove(self, val):
        """
        removes first instance of val found in the list starting from the head.
        If val is not present then a ValueError will be raised.
        """
        currentNode = self._head
        while currentNode is not None:
            if currentNode.val == val:
                if currentNode is self._head:
                    self.pop()
                elif currentNode is self._tail:
                    self.shift()
                else:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                    currentNode.prev = currentNode.next = None  # just in case
                    self._size -= 1
                return
            else:
                currentNode = currentNode.next
        raise ValueError("Value not found in the list")
