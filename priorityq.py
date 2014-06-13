from min_heap import MinHeap


class PrioritizedItem(object):
    def __init__(self, pri, value):
        self.pri, self.value = pri, value
        self._order = 0

    def __eq__(self, other):
        if hasattr(other, 'pri'):
            if self.pri == other.pri:
                if hasattr(other, '_order'):
                    return self._order == other._order
        return False

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __lt__(self, other):
        # this should cover __gt__ implicitly
        if hasattr(other, 'pri'):
            if self.pri == other.pri:
                if hasattr(other, '_order'):
                    return self._order < other._order
                else:
                    raise Exception(
                        "right-most object must have an _order attr")
            return self.pri < other.pri
        raise Exception("right-most object must have a pri attribute")

    def __gt__(self, other):
        # this should cover __gt__ implicitly
        if hasattr(other, 'pri'):
            if self.pri == other.pri:
                if hasattr(other, '_order'):
                    return self._order > other._order
                else:
                    raise Exception(
                        "right-most object must have an _order attr")
            return self.pri > other.pri
        raise Exception("right-most object must have a pri attribute")

    def __str__(self):
        return str(self.pri + ":" + self.value + ":" + self._order)


class PriorityQueue(object):
    def __init__(self):
        self._heap = MinHeap()
        self._num_inserted = 0

    def _gen_order(self):
        self._num_inserted += 1
        return self._num_inserted

    def insert(self, prioritized_item):
        prioritized_item._order = self. _gen_order()
        self._heap.push(prioritized_item)
        #print self._heap._print_list()

    def pop(self):
        return self._heap.pop()

    def peek(self):
        return self._heap.peek()
