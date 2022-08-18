from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode[{self.val}, {self.next}]"

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        else:
            return (self.val == other.val) and (self.next == other.next)


def initialize_single_linked_list(l: List) -> Optional[ListNode]:
    h = t = ListNode(l[0])
    for el in l[1:]:
        t.next = ListNode(el)
        t = t.next
    return h


# Given the head of a linked list, remove the nth node from the end of the list and return its head
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fakeroot = ListNode(0, head)
    # Create two pointers which are going to be n steps in between
    imiddle = iend = fakeroot

    # Move end pointer n steps ahead
    for i in range(n):
        iend = iend.next

    print(iend)

    # Move two pointers together until end pointer reaches the end
    while iend.next is not None:
        iend = iend.next
        imiddle = imiddle.next

    if imiddle.next is None:
        pass
    else:
        if imiddle.next.next is None:
            imiddle.next = None
        else:
            imiddle.next = imiddle.next.next
    return fakeroot.next


def test_5():
    l = initialize_single_linked_list([1, 2, 3, 4, 5])
    r = initialize_single_linked_list([1, 2, 3, 5])

    assert removeNthFromEnd(l, 2) == r


def test_1():
    l = initialize_single_linked_list([1])
    r = None

    assert removeNthFromEnd(l, 1) == r


def test_2():
    l = initialize_single_linked_list([1, 2])
    r = initialize_single_linked_list([1])

    assert removeNthFromEnd(l, 1) == r
