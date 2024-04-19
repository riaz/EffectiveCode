import pytest

from algo.linkedlist.single import MyLinkedList

def test_get_head():
    obj = MyLinkedList()
    obj.addAtHead(30)
    obj.addAtHead(20)
    obj.addAtHead(10)
    
    
    param_1 = obj.get(0)
    param_2 = obj.get(1)
    param_3 = obj.get(2)
    
    assert param_1 == 10
    assert param_2 == 20
    assert param_3 == 30

def test_get_tail():
    obj = MyLinkedList()
    
    obj.addAtTail(10)
    obj.addAtTail(20)
    obj.addAtTail(30)
    
    
    param_1 = obj.get(0)
    param_2 = obj.get(1)
    param_3 = obj.get(2)
    
    assert param_1 == 10
    assert param_2 == 20
    assert param_3 == 30    


def test_get_head_tail():
    obj = MyLinkedList()
    
    obj.addAtTail(20)

    param_1 = obj.get(0)

    obj.addAtHead(10)
    obj.addAtTail(30)
    
    
    param_2 = obj.get(0)
    param_3 = obj.get(1)
    param_4 = obj.get(2)
    
    assert param_1 == 20
    
    assert param_2 == 10
    assert param_3 == 20   
    assert param_4 == 30   

    
def test_delete_at_index():    
    obj = MyLinkedList()

    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)

    assert 2 == obj.get(1)

    obj.deleteAtIndex(1)

    assert 3 == obj.get(1)


def test_delete_at_index_small():    
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.deleteAtIndex(0)

def test_delete_at_index_med():    
    obj = MyLinkedList()
    
    obj.addAtHead(1)
    obj.addAtHead(3)
    obj.addAtIndex(1,2)

    assert 2 == obj.get(1)

    obj.deleteAtIndex(0)

    assert 2 == obj.get(0)
