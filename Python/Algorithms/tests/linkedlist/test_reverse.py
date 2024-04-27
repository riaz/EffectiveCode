from algo.linkedlist.reverse import reverse_iterative, reverse_recursive
from algo.linkedlist.node import Node
import random

from typing import List

def arr_to_ll(arr: List[int]) -> Node:
    """
    This is a helper function that converts arr to linkedlist
    """
    head = Node(0)
    tmp = head
    for val in arr:
        tmp.next = Node(val)
        tmp = tmp.next
    return head.next


def ll_to_arr(ll: Node) -> List[int]:
    """
    This is a helper function that converts linkedlist to arr
    """
    arr = []
    while ll:
        arr.append(ll.val)
        ll = ll.next
    return arr

def test_reverse_list():
    actual_arr = [1,2,3,4,5]
    actual_ll = arr_to_ll(actual_arr)

    expected_arr = actual_arr[::-1]
    
    assert expected_arr == ll_to_arr(reverse_iterative(actual_ll))


def test_reverse_list_random():
    # randomly sampling a list o
    size = random.randint(3, 100)
    actual_arr = random.sample(range(0,100000), size)
    actual_ll = arr_to_ll(actual_arr)
    expected_arr = actual_arr[::-1]
    
    assert expected_arr == ll_to_arr(reverse_iterative(actual_ll))    


def test_reverse_recursive_list_random():
    # randomly sampling a list o
    size = random.randint(3, 100)
    actual_arr = random.sample(range(0,100000), size)
    actual_ll = arr_to_ll(actual_arr)
    expected_arr = actual_arr[::-1]
    
    assert expected_arr == ll_to_arr(reverse_recursive(actual_ll))  