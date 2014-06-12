import pdb


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
        # put the last item in the root

        # compare the new root to it's children.  swap root with
        # smallest child, if it exists

        # move to smallest child.
        if len(self._list) == 0:
            return None
        else:
            top = self._list[0]
            # replace the root of the heap with the last element
            # of the last level
            self._swap(0, -1)
            # trim the root just moved to last position of list
            del self._list[-1]
            self._trickle_down(0)
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
        returns the list index of the smaller of a node's two children.
        Returns None if neither child is smaller or no children.
        If left = right, returns left.
        """
        lc_loc, rc_loc = self._find_left_child(p), self._find_right_child(p)
        has_lc, has_rc = lc_loc is not None, rc_loc is not None
        lc_val = rc_val = None
        if has_lc:
            lc_val = self._list[lc_loc]
        if has_rc:
            rc_val = self._list[rc_loc]
        # print "p is {}".format(p)
        # print "lc_loc is {}".format(lc_loc)
        # print "rc_loc is {}".format(rc_loc)
        # print "lc_val is {}".format(lc_val)
        # print "rc_val is {}".format(rc_val)
        # print "has_lc is {}".format(has_lc)
        # print "has_rc is {}".format(has_rc)

        # case1 where we have no left child or right child
        if not (has_lc or has_rc):
            # print "in case1"
            return None
        # case2 where we have both left and right child
        elif (has_lc and has_rc):
            # print "in case2"
            if (lc_val <= rc_val):
                return lc_loc if lc_val < self._list[p] else None
            else:
                return rc_loc if rc_val < self._list[p] else None
        # case3 where we only have left child
        elif has_lc:
            # print "in case3"
            return lc_loc if lc_val < self._list[p] else None
        # case4 where we only have right child
        else:
            # print "in case4"
            return rc_loc if rc_val < self._list[p] else None

    def _trickle_down(self, n):
        """
        compares node n to it's children,
        if child exists, swaps with smallest child
        calls _trickle_down on child's old location
        otherwise it returns.
        """
        print "n={}".format(n)
        sc = self._smaller_child(n)
        print "outside of while loop, sc={}".format(sc)
        # pdb.set_trace()
        if sc is not None:
            self._swap(n, sc)
            print "just swapped, sc={} calling trickle_down(sc)".format(sc)
            sc = self._smaller_child(sc)
            if sc is None:
                return
            else:
                self._trickle_down(sc)

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

    def _print_list(self):
        """
        prints the list
        """
        print self._list
