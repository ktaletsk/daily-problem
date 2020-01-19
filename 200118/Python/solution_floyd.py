class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fastPointer = head
        slowPointer = head
        
        while(True):
            if fastPointer == None or slowPointer == None:
                return False

            if fastPointer.next == None:
                return False
            else:
                if fastPointer.next.next == None:
                    return False
                else:
                    fastPointer = fastPointer.next.next
            
            if slowPointer.next == None:
                return False
            else:
                slowPointer = slowPointer.next
        
            if id(fastPointer)==id(slowPointer):
                return True

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