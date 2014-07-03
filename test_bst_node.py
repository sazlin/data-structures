from bst import BSTNode


def test_init():
    parent_node = BSTNode(0)
    b = BSTNode(1)
    c = BSTNode(3)
    a = BSTNode(2, parent=parent_node, left_child=b, right_child=c)
    assert a.value == 2
    assert a.left_child == b
    assert a.right_child == c
    assert a.parent == parent_node


def test_get_value():
    node = BSTNode(2)
    assert node.get_value() == 2


def test_set_value():
    node = BSTNode(1)
    node.set_value(2)
    assert node.get_value() == 2


def test_get_set_parent():
    parent_node = BSTNode(0)
    node = BSTNode(1)
    assert node.get_parent() is None
    node.set_parent(parent_node)
    assert node.get_parent() == parent_node


def test_get_set_left_child():
    left_child = BSTNode(0)
    node = BSTNode(1)
    assert node.get_left_child() is None
    node.set_left_child(left_child)
    assert node.get_left_child() == left_child


def test_get_set_right_child():
    right_child = BSTNode(0)
    node = BSTNode(1)
    assert node.get_right_child() is None
    node.set_right_child(right_child)
    assert node.get_right_child() == right_child


def test_greater_than():
    big_node = BSTNode(5)
    little_node = BSTNode(-5)
    assert big_node.greater_than(little_node)


def test_less_than():
    little_node = BSTNode(0)
    big_node = BSTNode(40)
    assert little_node.less_than(big_node)


def test_equals():
    node1 = BSTNode(5)
    node2 = BSTNode(5)
    assert node1.equals(node2)
    assert node2.equals(node1)


def test_greater_than_equals():
    node1 = BSTNode(4)
    node2 = BSTNode(4)
    node3 = BSTNode(6)
    assert node2.greater_than_equals(node1)
    assert node3.greater_than_equals(node2)


def test_less_than_equals():
    node1 = BSTNode(3)
    node2 = BSTNode(3)
    node3 = BSTNode(1)
    assert node2.less_than_equals(node1)
    assert node3.less_than_equals(node2)
