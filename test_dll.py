import pytest
from dll import DLinkedList


@pytest.fixture(scope='function')
def create_list():
    test_list = DLinkedList()
    test_list.insert(0)
    return test_list


def test_init():
    test_list = DLinkedList()
    assert test_list or test_list._head or test_list._tail is not None


def test_insert_1(create_list):
    test_list = create_list
    assert test_list._size == 1


def test_insert_2(create_list):
    assert create_list._head is not None


def test_insert_3(create_list):
    assert create_list._tail is not None


def test_insert_4(create_list):
    assert (create_list._head.val == 0) and (create_list._tail.val == 0)


def test_insert_5(create_list):
    create_list.insert(1)
    assert (create_list._tail.val == 0) and (create_list._head.val == 1)


def test_append_1(create_list):
    create_list.append(1)
    assert (create_list._tail.val == 1) and (create_list._head.val == 0)


def test_append_2(create_list):
    create_list.append(1)
    assert create_list._size == 2


def test_pop_1(create_list):
    assert create_list.pop() == 0


def test_pop_2(create_list):
    create_list.pop()
    assert create_list._size == 0


def test_pop_3(create_list):
    create_list.pop()
    assert (create_list._head is None) and (create_list._tail is None)


def test_pop_4():
    test_list = DLinkedList()
    assert test_list.pop() is None


def test_shift_1(create_list):
    assert create_list.shift() == 0


def test_shift_2(create_list):
    create_list.shift()
    assert create_list._size == 0


def test_shift_3(create_list):
    create_list.shift()
    assert (create_list._head is None) and (create_list._tail is None)


def test_shift_4():
    test_list = DLinkedList()
    assert test_list.shift() is None


def test_remove_1(create_list):
    create_list.remove(0)
    assert create_list._size == 0


def test_remove_2(create_list):
    create_list.insert(1)
    create_list.insert(0)
    # should remove the top-most insertion, such that next pop() is 1
    create_list.remove(0)
    assert create_list.pop() == 1
    assert create_list.pop() == 0


def test_remove_3(create_list):
    with pytest.raises(ValueError):
        create_list.remove(348252834)
