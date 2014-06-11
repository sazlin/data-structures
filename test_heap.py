import pytest


@pytest.fixture(scope='function')
def create_empty_min_heap():
    from min_heap import MinHeap
    empty_min_heap = MinHeap()
    return empty_min_heap


@pytest.fixture(scope='function')
def create_2_item_heap():
    from min_heap import MinHeap
    two_item_heap = MinHeap()
    two_item_heap.push(1)
    two_item_heap.push(2)
    return two_item_heap


@pytest.fixture(scope='function')
def create_5_item_heap():
    from min_heap import MinHeap
    five_item_heap = MinHeap()
    five_item_heap.push(1)
    five_item_heap.push(2)
    five_item_heap.push(3)
    five_item_heap.push(4)
    five_item_heap.push(5)
    return five_item_heap


def test_init_no_iterable():
    from min_heap import MinHeap
    mh = MinHeap()
    assert mh is not None


def test_init_with_sorted_iterable(l=[1, 2, 3, 4, 5]):
    from min_heap import MinHeap
    mh = MinHeap(l)
    assert mh._list[0] == 1
    assert mh._list[1] == 2
    assert mh._list[2] == 3
    assert mh._list[3] == 4
    assert mh._list[4] == 5


def test_init_with_unsorted_iterable(l=[5, 2, 1, 4, 3]):
    from min_heap import MinHeap
    mh = MinHeap(l)
    assert mh._list[0] == 1
    assert mh._list[1] == 2
    assert mh._list[2] == 3
    assert mh._list[3] == 4
    assert mh._list[4] == 5


def test_push_on_empty_heap(create_empty_min_heap):
    create_empty_min_heap.push(1)
    assert create_empty_min_heap._list[0] == 1


def test_push_larger_on_small_heap(create_2_item_heap):
    create_2_item_heap.push(3)
    assert create_2_item_heap._list[0] == 1
    assert create_2_item_heap._list[1] == 2
    assert create_2_item_heap._list[2] == 3


def test_push_smaller_on_small_heap(create_2_item_heap):
    create_2_item_heap.push(0)
    # The correct results can be confusing.  Draw the operation to see.
    assert create_2_item_heap._list[0] == 0
    assert create_2_item_heap._list[1] == 2
    assert create_2_item_heap._list[2] == 1


def test_push_larger_on_large_heap(create_5_item_heap):
    create_5_item_heap.push(6)
    assert create_5_item_heap._list[0] == 1
    assert create_5_item_heap._list[1] == 2
    assert create_5_item_heap._list[2] == 3
    assert create_5_item_heap._list[3] == 4
    assert create_5_item_heap._list[4] == 5
    assert create_5_item_heap._list[5] == 6


def test_push_smaller_on_large_heap(create_5_item_heap):
    create_5_item_heap.push(0)
    # The correct results can be confusing.  Draw the operation to see.
    assert create_5_item_heap._list[0] == 0
    assert create_5_item_heap._list[1] == 2
    assert create_5_item_heap._list[2] == 1
    assert create_5_item_heap._list[3] == 4
    assert create_5_item_heap._list[4] == 5
    assert create_5_item_heap._list[5] == 3


def test_pop_on_empty_heap(create_empty_min_heap):
    assert create_empty_min_heap.pop() is None


def test_pop_on_small_heap(create_2_item_heap):
    assert create_2_item_heap.pop() == 1
    assert create_2_item_heap.pop() == 2


def test_pop_on_large_heap(create_5_item_heap):
    for i in range(len(create_5_item_heap)):
        assert create_5_item_heap.pop() == i + 1


def test_peek_on_empty_heap(create_empty_min_heap):
    assert create_empty_min_heap.peek() is None


def test_peek_on_not_empty_heap(create_2_item_heap):
    assert create_2_item_heap.peek() == 1
    assert create_2_item_heap.peek() == 1


def test_play():
    test_list = range(1, 6)
    for x in range(len(test_list)):
        assert test_list[x] == x + 1
