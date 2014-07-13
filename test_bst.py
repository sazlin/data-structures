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


def test_pre_order_1(empty_bst):
    bst = empty_bst
    with pytest.raises(StopIteration):
        bst.pre_order().next()


def test_pre_order_2(optimal_bst):
    bst = optimal_bst
    expected = [6, 4, 2, 5, 8, 7, 9]
    actual = [i for i in bst.pre_order()]
    assert actual == expected


def test_pre_order_3(degenerate_bst):
    bst = degenerate_bst
    expected = [6, 4, 2]
    actual = [i for i in bst.pre_order()]
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
    #[6, 4, 8, 2, 5, 7, 9]
    bst = optimal_bst
    leaf_test_val = 7
    non_leaf_test_val = 4
    assert bst.contains(leaf_test_val)
    assert bst.contains(non_leaf_test_val)
    assert bst.delete(leaf_test_val) is None
    assert [val for val in bst.breadth_first()] == [6,4,8,2,5,9]
    assert bst.delete(non_leaf_test_val) is None
    assert [val for val in bst.breadth_first()] == [6,5,8,2,9]


def test_delete_node_3(degenerate_bst):
    bst = degenerate_bst
    leaf_test_val = 2
    non_leaf_test_val = 6
    assert bst.contains(leaf_test_val)
    assert bst.contains(non_leaf_test_val)
    assert bst.delete(leaf_test_val) is None
    assert [val for val in bst.breadth_first()] == [6,4]
    assert bst.delete(non_leaf_test_val) is None
    assert [val for val in bst.breadth_first()] == [4]


def test_delete_node_4(degenerate_bst):
    bst = degenerate_bst
    test_val = 777
    assert not bst.contains(test_val)
    before_delete = [val for val in bst.in_order()]
    assert bst.delete(777) is None
    after_delete = [val for val in bst.in_order()]
    assert before_delete == after_delete


def test_avl_1(empty_bst):
    bst = empty_bst
    assert not bst.avl()


def test_avl_2(optimal_bst):
    #Show that avl() doesn't change an already balanced tree
    bst = optimal_bst
    expected = [6, 4, 8, 2, 5, 7, 9]
    bst.avl()
    actual = [item for item in bst.breadth_first()]
    assert actual == expected


def test_avl_3(degenerate_bst):
    #Show that a simple degenerate tress is balanced with avl()
    bst = degenerate_bst
    expected = [4, 2, 6]
    bst.avl()
    actual = [item for item in bst.breadth_first()]
    assert expected == actual

def test_avl_4(optimal_bst):
    #Show avl() in action for insert
    bst = optimal_bst
    bst.insert(15)
    bst.insert(12)
    expected = [6, 4, 8, 2, 5, 7, 12, 9, 15]
    actual = [item for item in bst.breadth_first()]
    assert expected == actual


def test_avl_5(optimal_bst):
    #show avl() in action for delete
    bst = optimal_bst
    bst.insert(15)
    bst.delete(7)
    expected = [6, 4, 9, 2, 5, 8, 15]
    actual = [item for item in bst.breadth_first()]
    assert expected == actual

def test_rotate_left_1(empty_bst):
    bst = empty_bst
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    new_root = bst._rotate_left(bst.root)
    assert new_root.value == 6
    assert new_root.left.value == 4
    assert new_root.right.value == 8
    assert new_root.left.left is None
    assert new_root.left.right is None
    assert new_root.right.left is None
    assert new_root.right.right is None

def test_rotate_left_1(empty_bst):
    bst = empty_bst
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    bst.insert(10)
    new_root = bst._rotate_left(bst.root)
    assert new_root.value == 6
    assert new_root.left.value == 4
    assert new_root.right.value == 8
    assert new_root.left.left is None
    assert new_root.left.right is None
    assert new_root.right.left is None
    assert new_root.right.right.value == 10

def test_rotate_right_1(empty_bst):
    bst = empty_bst
    bst.insert(8)
    bst.insert(6)
    bst.insert(4)
    bst.insert(1)
    new_root = bst._rotate_right(bst.root)
    assert new_root.value == 6
    assert new_root.left.value == 4
    assert new_root.right.value == 8
    assert new_root.left.left.value == 1
    assert new_root.left.right is None
    assert new_root.right.left is None
    assert new_root.right.right is None
