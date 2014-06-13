import pytest
from priorityq import PriorityQueue
from priorityq import PrioritizedItem


@pytest.fixture(scope="function")
def get_pq():
    pq = PriorityQueue()
    pq.insert(PrioritizedItem(3, 'low pri'))
    pq.insert(PrioritizedItem(1, 'first pri'))
    pq.insert(PrioritizedItem(3, 'also low pri'))
    pq.insert(PrioritizedItem(2, 'second pri'))
    pq.insert(PrioritizedItem(3, 'another low pri'))
    return pq


def test_gen_order_1():
    pq = PriorityQueue()
    assert pq._gen_order() == 1
    assert pq._gen_order() == 2


def test_insert_1(get_pq):
    assert len(get_pq._heap._list) == 5


def test_pop_1(get_pq):
    assert get_pq._heap.pop().value == 'first pri'


def test_pop_2(get_pq):
    get_pq.pop()
    assert get_pq.pop().value == 'second pri'


def test_pop_3(get_pq):
    """Ensure that items with same pri pop() in FIFO order"""
    get_pq.pop()
    get_pq.pop()
    assert get_pq.pop().value == 'low pri'


def test_peek_1(get_pq):
    assert get_pq._heap.peek().value == 'first pri'


def test_peek_2(get_pq):
    get_pq.pop()
    assert get_pq.peek().value == 'second pri'


def test_peek_3(get_pq):
    get_pq.pop()
    get_pq.pop()
    assert get_pq.peek().value == 'low pri'


def test_peek_4(get_pq):
    get_pq.peek()
    assert get_pq._heap.peek().value == 'first pri'
