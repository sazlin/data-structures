import timeit
from functools import total_ordering


@total_ordering
class BSTNode(object):

    def __init__(self, value, parent=None, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


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
            left_depth = self._depth(current_depth + 1, local_root.left)
        if local_root.right:
            right_depth = self._depth(current_depth + 1, local_root.right)
        return max(current_depth, left_depth, right_depth)

    def balance(self):
        return self._balance(self.root)

    def _balance(self, node):
        ret_val = 0
        if node is None:
            return ret_val
        if node.left:
            ret_val += self._depth(1, node.left)
        if node.right:
            ret_val -= self._depth(1, node.right)
        return ret_val

    def pre_order(self):
            return self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            yield node.value
            for left_subtree_val in self._pre_order(node.left):
                yield left_subtree_val
            for right_subtree_val in self._pre_order(node.right):
                yield right_subtree_val

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, node):
        if node:
            for left_subtree_val in self._post_order(node.left):
                yield left_subtree_val
            for right_subtree_val in self._post_order(node.right):
                yield right_subtree_val
            yield node.value

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        if node:
            for left_subtree_value in self._in_order(node.left):
                yield left_subtree_value
            yield node.value
            for right_subtree_value in self._in_order(node.right):
                yield right_subtree_value

    def breadth_first(self):
        # adapted from
        # www.geeksforgeeks.org/level-order-tree-traversal/
        height = self.depth()
        for level in xrange(1, height+1):
            for value in self._yield_level(self.root, level):
                yield value

    def _yield_level(self, root, level):
        if root is None:
            raise StopIteration()
        if level == 1:
            yield root.value
        else:
            for left_next_level in self._yield_level(root.left, level-1):
                yield left_next_level
            for right_next_level in self._yield_level(root.right, level-1):
                yield right_next_level

    def delete(self, val):
        self.root = self._delete(val, self.root)
        return None

    def _delete(self, val, node):

        def _min_val(node):
            if node.left:
                return _min_val(node.left)
            else:
                return node.value

        if not node:
            # no child here, so return
            return None

        if node.value == val:
            self._size -= 1
            if node.left and node.right:
                # both left and right children exist
                node.value = _min_val(node.right)
                node.right = self._delete(node.value, node.right)
                return node
            elif node.left and not node.right:
                # only left child exists
                return node.left
            elif not node.left and node.right:
                # only right child exists
                return node.right
            else:
                # no children
                return None
        elif node.value < val:
            if node.right:
                node.right = self._delete(val, node.right)
            return node
        else:
            if node.left:
                node.left = self._delete(val, node.left)
            return node

if __name__ == '__main__':

    test_runs = 100000

    balanced_time = timeit.timeit('''
    balanced_contents = [
        50, 40, 60, 35, 45, 55, 65, 31, 39, 41, 49, 51, 59, 61, 69]
    BinarySearchTree(balanced_contents).contains(69)
    ''', setup="from __main__ import BinarySearchTree", number=test_runs)

    unbalanced_time = timeit.timeit('''
    unbalanced_contents = [
        31, 35, 39, 40, 41, 45, 49, 50, 51, 55, 59, 60, 61, 65, 69]
    BinarySearchTree(unbalanced_contents).contains(69)
    ''', setup="from __main__ import BinarySearchTree", number=test_runs)

    print "Time for a balanced tree (best case) is: {}\n".format(balanced_time)
    print "Time for an unbalanced tree (worst case) is: {}\n".format(
        unbalanced_time)
