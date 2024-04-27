"""
This file features reversing a linkedlist both iteratively as well as recursion
"""
from algo.linkedlist.node import Node
from typing import List

def reverse_iterative(head : Node) -> Node:
    left = None
    while head:
        right = head.next
        head.next = left
        left = head
        head = right
    return left

def reverse_recursive(head: Node) -> Node:
    """
    Recursive method to reverse a linkedlist
    """
    if not head or not head.next:
        # base condition
        return head

    left = head
    right = reverse_recursive(left.next)
    left.next.next = left
    left.next = None
    return right