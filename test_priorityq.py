import pytest
from priorityq import PriorityQueue
from priorityq import PrioritizedItem


@pytest.fixture(scope="function")
def get_pq():
    pq = PriorityQueue()
    pq.insert(PrioritizedItem(3, 'A'))
    pq.insert(PrioritizedItem(1, 'B'))
    pq.insert(PrioritizedItem(3, 'C'))
    pq.insert(PrioritizedItem(2, 'D'))
    pq.insert(PrioritizedItem(3, 'E'))
    return pq


def test_gen_order_1():
    pq = PriorityQueue()
    assert pq._gen_order() == 1
    assert pq._gen_order() == 2


def test_insert_1(get_pq):
    assert len(get_pq._heap._list) == 5


def test_pop_1(get_pq):
    assert get_pq._heap.pop().value == 'B'


def test_pop_2(get_pq):
    get_pq.pop()
    assert get_pq.pop().value == 'D'


def test_pop_3(get_pq):
    """Ensure that items with same pri pop() in FIFO order"""
    get_pq.pop()
    get_pq.pop()
    assert get_pq.pop().value == 'A'
    assert get_pq.pop().value == 'C'


def test_peek_1(get_pq):
    assert get_pq._heap.peek().value == 'B'
    assert get_pq._heap.peek().value == 'B'


def test_peek_2(get_pq):
    get_pq.pop()
    assert get_pq.peek().value == 'D'


def test_peek_3(get_pq):
    get_pq.pop()
    get_pq.pop()
    assert get_pq.peek().value == 'A'


def test_peek_4(get_pq):
    get_pq.peek()
    assert get_pq._heap.peek().value == 'B'
