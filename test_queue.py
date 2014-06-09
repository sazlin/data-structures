from queue import Queue


def test_init():
    test_queue = Queue()
    assert test_queue is not None


def test_size_is_0():
    test_queue = Queue()
    assert test_queue.size() == 0


def test_size_is_1():
    test_queue = Queue()
    test_queue.enqueue(1)
    assert test_queue.size() == 1


def test_size_2():
    test_queue = Queue()
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.dequeue()
    assert test_queue.size() == 1


def test_enqueue_1():
    test_queue = Queue()
    test_queue.enqueue(1)
    assert test_queue.dequeue() == 1


def test_dequeue_1():
    test_queue = Queue()
    test_queue.enqueue(1)
    test_queue.dequeue()
    assert test_queue.size() == 0
