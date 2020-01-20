# Doubly-linked list
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def is_palindrome(node):
    # Find the end of the list (Complexity: O(n))
    tail = node
    while tail.next != None:
        tail = tail.next
    
    # Iterate from both end of the list and check if values are the same all the time (Complexity: O(n))
    while node.next != None:
        # Check that i-th element is equal to (n-i)-th element
        if node.val != tail.val:
            return False

        # Move 1 element along the list
        node = node.next
        tail = tail.prev

    # If the end was reached, that means we confirmed palindrome
    return True

# Helper function to build doubly-linked lists
def build_doubly_linked_list(values):
    n = len(values)
    result = [Node(value) for value in values]
    for i in range(n):
        if i>0:
            result[i].prev = result[i-1]
        if i<n-1:
            result[i].next = result[i+1]
        
    return result[0]

# Test the solution
def test():
    assert is_palindrome(build_doubly_linked_list(['a', 'b', 'b', 'a'])) == True
    assert is_palindrome(build_doubly_linked_list(['a', 'b', 'c', 'b', 'a'])) == True
    assert is_palindrome(build_doubly_linked_list(['a', 'a'])) == True
    assert is_palindrome(build_doubly_linked_list(['a'])) == True
    assert is_palindrome(build_doubly_linked_list(['a', 'b'])) == False