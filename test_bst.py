from bst import BinarySearchTree
# from bst import BSTNode
import pytest


@pytest.fixture(scope="function")
def empty_bst():
    return BinarySearchTree()


@pytest.fixture(scope="function")
def optimal_bst():
    return BinarySearchTree([6, 4, 8, 2, 5, 7, 9])


@pytest.fixture(scope="function")
def degenerate_bst():
    return BinarySearchTree([6, 4, 2])


def test_bst_init():
    bstree = BinarySearchTree()
    assert bstree is not None
    assert bstree.size() == 0


def test_bst_init_size(empty_bst):
    assert empty_bst.size() == 0


def test_insert():
    bst = BinarySearchTree([6, 4, 8, 6])
    assert bst.root.value == 6
    assert bst.root.left.value == 4
    assert bst.root.right.value == 8
    assert bst.size() == 3


def test_contains_empty_BST(empty_bst):
    assert not empty_bst.contains(4)


def test_contains_optimal(optimal_bst):
    contents = [6, 4, 8, 2, 5, 7, 9]
    assert [optimal_bst.contains(item) for item in contents]
    assert not optimal_bst.contains(20)


def test_depth(empty_bst):
    assert empty_bst.depth() == 0


def test_depth_optimal(optimal_bst):
    assert optimal_bst.depth() == 3


def test_depth_degenerate(degenerate_bst):
    assert degenerate_bst.depth() == 3


def test_balance_empty(empty_bst):
    assert empty_bst.balance() == 0


def test_balance_optimal(optimal_bst):
    assert optimal_bst.balance() == 0


def test_balance_left_heavy(degenerate_bst):
    assert degenerate_bst.balance() == 2


def test_balance_right_heavy():
    contents = [6, 8, 10]
    bst = BinarySearchTree(contents)
    assert bst.balance() == -2


def test_post_order_1(empty_bst):
    bst = empty_bst
    with pytest.raises(StopIteration):
        bst.post_order().next()


def test_post_order_2(optimal_bst):
    bst = optimal_bst
    expected = [2, 5, 4, 7, 9, 8, 6]
    actual = [i for i in bst.post_order()]
    assert actual == expected


def test_in_order_1(empty_bst):
    bst = empty_bst
    expected = []
    actual = [item for item in bst.in_order()]
    assert expected == actual


def test_in_order_2(optimal_bst):
    bst = optimal_bst
    expected = [2, 4, 5, 6, 7, 8, 9]
    actual = [item for item in bst.in_order()]
    assert expected == actual


def test_in_order_3(degenerate_bst):
    bst = degenerate_bst
    expected = [2, 4, 6]
    actual = [item for item in bst.in_order()]
    assert expected == actual


def test_bf_1(empty_bst):
    expected = []
    actual = [item for item in empty_bst.breadth_first()]
    assert expected == actual


def test_bf_2(optimal_bst):
    expected = [6, 4, 8, 2, 5, 7, 9]
    actual = [item for item in optimal_bst.breadth_first()]
    assert expected == actual


def test_bf_3(degenerate_bst):
    expected = [6, 4, 2]
    actual = [item for item in degenerate_bst.breadth_first()]
    assert expected == actual

def test_delete_node_1(empty_bst):
    bst= empty_bst
    assert bst.delete(777) is None


def test_delete_node_2(optimal_bst):
    bst = optimal_bst
    test_val = 123
    assert not bst.contains(test_val)
    bst.insert(test_val)
    assert bst.contains(test_val)
    assert bst.delete(777) is None
    assert not bst.contains(test_val)

def test_delete_node_3(degenerate_bst):
    bst = degenerate_bst
    test_val = 123
    assert not bst.contains(test_val)
    bst.insert(test_val)
    assert bst.contains(test_val)
    assert bst.delete(777) is None
    assert not bst.contains(test_val)
