class MinHeap(object):

    def __init__(self, iterable=None):
        """
        Initialize a heap, if iterable is passed initialize heap to
        contents of iterable, otherwise initialize empty heap.
        """
        if iterable is None:
            self._list = []
        else:
            self._list = iterable
            self._heapify()

    def push(self, val):
        """
        Puts a new value into the heap, maintaining the heap property.
        """
        pass

    def pop(self):
        """
        Removes the "top" value in the heap, maintaining the heap property.
        """
        pass

    def peek(self):
        """
        Returns the value of the top of the heap, without removal.
        """
    def _heapify(self):
        """
        turns the list into a heap.
        """
        pass

    def _swap(self, i, j):
        """
        swaps the items in _list at indexes i and j.
        """
        self._list[i], self._list[j] = self._list[j], self._list[i]

    def _find_parent(self, i):
        """
        given an index i, finds the index of the parent of i.
        """
        return None if i == 0 else (i - 1) // 2

    def _find_left_child(self, i):
        """
        given an index i, finds the index of the left child of i.
        """
        pass

    def _find_right_child(self, i):
        """
        given an index i, finds the index of the right child of i
        """
        pass
