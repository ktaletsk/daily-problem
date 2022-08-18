from typing import Optional, List
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode[{self.val}, {self.next}]"

    def __eq__(self, other) -> bool:
        return (self.val == other.val) and (self.next == other.next)


def initialize_single_linked_list(l: List) -> Optional[ListNode]:
    n = ListNode(l[-1])
    for el in l[len(l) - 2 :: -1]:
        p = ListNode(el, n)
        n = p
    return n


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    imiddle = iend = head
    while iend.next is not None:
        iend = iend.next
        if iend.next is not None:
            iend = iend.next
        imiddle = imiddle.next
    return imiddle


def test_5():
    full = initialize_single_linked_list([1, 2, 3, 4, 5])
    middle = initialize_single_linked_list([3, 4, 5])

    assert middleNode(full) == middle


def test_6():
    full = initialize_single_linked_list([1, 2, 3, 4, 5, 6])
    middle = initialize_single_linked_list([4, 5, 6])

    assert middleNode(full) == middle
