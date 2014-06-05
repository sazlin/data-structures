import pytest
from linked_list import l_list


@pytest.fixture(scope='function')
def create_list():
    test_list = l_list()
    test_list.insert(1)
    test_list.insert(2)
    return test_list


def test_init():
    test_list = None
    test_list = l_list()
    assert test_list is not None
    assert test_list.size() == 0
    assert test_list.pop() is None


def test_insert(create_list):
    test_list = create_list
    initial_size = test_list.size()
    test_value = 321
    test_list.insert(test_value)
    assert test_list.size() == initial_size + 1
    assert test_list.pop() == test_value


def test_pop(create_list):
    test_list = create_list
    initial_size = test_list.size
    test_val = 65356345
    test_list.insert(test_val)
    assert test_list.pop() == test_val
    assert test_list.size == initial_size


def test_size(create_list):
    test_list = create_list
    assert test_list.size() == 2


def test_print(create_list):
    test_list = create_list
    expected = "(2, 1)"
    assert test_list._print() == expected


def test_search(create_list):
    test_list = create_list
    search_val1 = 432625723
    search_val2 = 989802374
    search_val3 = -235236324
    test_list.insert(search_val1)
    test_list.insert(search_val2)
    test_list.insert(search_val3)
    assert test_list.search(search_val2).val == search_val2
    assert test_list.search(-99999) is None


def test_remove(create_list):
    test_list = create_list
    test_val = 923423748
    test_node = test_list.insert(test_val)
    assert test_list.search(test_val) is not None
    test_list.remove(test_node)
    assert test_list.search(test_val) is None
