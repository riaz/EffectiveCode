import pytest

from algo.linkedlist.stack import Stack

def test_init():
    stack = Stack()
    assert stack._size == 0
    assert stack._head is None

def test_len():
    stack = Stack()
    assert stack.len() == 0
    stack.push(1)
    assert stack.len() == 1
    stack.push(2)
    assert stack.len() == 2

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

def test_push():
    stack = Stack()
    stack.push(1)
    assert stack._head._element == 1
    assert stack._size == 1
    stack.push(2)
    assert stack._head._element == 2
    assert stack._head._next._element == 1
    assert stack._size == 2

def test_top():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.top()
    stack.push(1)
    assert stack.top() == 1
    stack.push(2)
    assert stack.top() == 2

def test_pop():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
    stack.push(1)
    assert stack.pop() == 1
    assert stack._size == 0
    assert stack._head is None
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.top() == 1
    assert stack._size == 1