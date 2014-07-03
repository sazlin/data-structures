import timeit
from functools import total_ordering


@total_ordering
class BSTNode(object):

    def __init__(self, value, parent=None, left_child=None, right_child=None):
        self.value = value
        self.parent = parent
        self.left = left_child
        self.right = right_child

    def __lt__(self, other):
        return self._value < other.get_value()

    def __eq__(self, other):
        return self._value == other.get_value()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None


class BinarySearchTree(object):

    def __init__(self, values=None):
        self._size = 0
        self.root = None
        if values:
            [self.insert(val) for val in values]

    def size(self):
        return self._size

    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
            self._size += 1
            return
        current_node = self.root
        while True:
            if current_node.value > val:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(val)
                    self._size += 1
                    break
            elif current_node.value < val:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(val)
                    self._size += 1
                    break
            else:
                # val is already in BST
                break

    def contains(self, val):
        if self.root is None:
            return False
        current_node = self.root
        while True:
            if current_node.value > val:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    return False
            elif current_node.value < val:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    return False
            else:
                return True

    def depth(self):
        if self.root is None:
            return 0
        return self._depth(1, self.root)

    def _depth(self, current_depth, local_root):
        left_depth = right_depth = 0
        if local_root.left:
            left_depth = self._depth(current_depth+1, local_root.left)
        if local_root.right:
            right_depth = self._depth(current_depth+1, local_root.right)
        return max(current_depth, left_depth, right_depth)

    def balance(self):
        ret_val = 0
        if self.root is None:
            return ret_val
        if self.root.left:
            ret_val += self._depth(1, self.root.left)
        if self.root.right:
            ret_val -= self._depth(1, self.root.right)
        return ret_val

    def in_order(self):

        def _in_order(node):
            if not node:
                yield None
            yield _in_order(node.left)
            yield node.value
            yield _in_order(node.right)

        return _in_order(self.root)



if __name__ == '__main__':

    test_runs = 100000

    balanced_time = timeit.timeit('''
    balanced_contents = [50, 40, 60, 35, 45, 55, 65, 31, 39, 41, 49, 51, 59, 61, 69]
    BinarySearchTree(balanced_contents).contains(69)
    ''', setup="from __main__ import BinarySearchTree", number=test_runs)

    unbalanced_time = timeit.timeit('''
    unbalanced_contents = [31, 35, 39, 40, 41, 45, 49, 50, 51, 55, 59, 60, 61, 65, 69]
    BinarySearchTree(unbalanced_contents).contains(69)
    ''', setup="from __main__ import BinarySearchTree", number=test_runs)

    print "Time for a balanced tree (best case) is: {}\n".format(balanced_time)
    print "Time for an unbalanced tree (worst case) is: {}\n".format(unbalanced_time)
