class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        s = set()
        while(head != None):
            if id(head) not in s:
                s.add(id(head))
            else:
                return True
            head = head.next
        
        return False

def test_loop():
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(2)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail
    testTail.next = node1

    assert Solution().hasCycle(testHead) == True

def test_no_loop():
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(2)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    assert Solution().hasCycle(testHead) == False

def test_empty_list():
    testHead = None

    assert Solution().hasCycle(testHead) == False