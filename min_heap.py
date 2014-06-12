class MinHeap(object):

    def __init__(self, iterable=None):
        """
        Initialize a heap, if iterable is passed initialize heap to
        contents of iterable, otherwise initialize empty heap.
        """
        self._list = []
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, val):
        """
        Puts a new value into the heap, maintaining the heap property.
        """
        self._list.append(val)
        # print "in push, _list is: {}".format(self._list)
        self._percolate_up(len(self._list) - 1)

    def pop(self):
        """
        Removes the "top" value in the heap, maintaining the heap property.
        """
        if len(self._list) == 0:
            return None
        else:
            top = self._list[0]
            # replace the root of the heap with the last element
            # of the last level
            self._swap(0, -1)
            # trim the root just moved to last position of list
            del self._list[-1]
            i = 0
            has_smaller = True
            while has_smaller:
                smlr_idx = self._smaller_child(i)
                if smlr_idx is None:
                    break
                else:
                    self._swap(i, smlr_idx)
                    i = smlr_idx
            return top

    def peek(self):
        """
        returns the value of the top node without removing it.
        """
        if len(self._list) == 0:
            return None
        else:
            return self._list[0]

    def _smaller_child(self, p):
        """
        returns the smaller of a node's two children.  Returns None if
        neither child is smaller.  If left = right, returns left.
        """

    def _heapify(self, p):
        """
        turns an tree into a heap efficiently
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
        child = (2 * i) + 1
        return None if child >= len(self._list) else child

    def _find_right_child(self, i):
        """
        given an index i, finds the index of the right child of i
        """
        child = (2 * i) + 2
        return None if child >= len(self._list) else child

    def _percolate_up(self, i):
        """
        percolates up the value at index i
        """
        parent_idx = self._find_parent(i)
        # print "in _percolate_up({0}) and parent_idx is {1}".format(
        #    i, parent_idx)
        if parent_idx is None or self._list[i] >= self._list[parent_idx]:
            return
        else:
            self._swap(i, parent_idx)
            self._percolate_up(parent_idx)
