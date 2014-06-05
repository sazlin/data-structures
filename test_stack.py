import pytest
from stack import Stack
from stack import EmptyStackError


@pytest.fixture(scope='function')
def create_stack():
    test_stack = Stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    return test_stack


def test_init():
    test_stack = Stack()
    assert test_stack is not None
    with pytest.raises(EmptyStackError):
        test_stack.pop()


def test_pop(create_stack):
    """test pop"""
    test_stack = create_stack
    assert test_stack.pop() == 3
    assert test_stack.pop() == 2
    assert test_stack.pop() == 1
    with pytest.raises(EmptyStackError):
        test_stack.pop()


def test_push():
    """test push"""
    test_stack = Stack()
    with pytest.raises(EmptyStackError):
        test_stack.pop()
    test_stack.push(3)
    test_stack.push(2)
    test_stack.push(1)
    assert test_stack.pop() == 1
    assert test_stack.pop() == 2
    assert test_stack.pop() == 3
