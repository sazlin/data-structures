from linked_list import l_list


class EmptyStackError(Exception):
    """The basic format of this is from a stackoverflow thread"""

    def __init__(self, message):
        Exception.__init__(self, message)


class Stack(object):
    """This class implements a basic stack with push and pop functions"""

    def __init__(self):
        """initialize the Stack object"""
        self._ll = l_list()

    def push(self, n):
        """pushes a value onto the stack"""
        self._ll.insert(n)

    def pop(self):
        """pops a value from the stack and returns the value"""
        if self._ll.size() == 0:
            raise EmptyStackError("the stack is empty")
        else:
            return self._ll.pop()
