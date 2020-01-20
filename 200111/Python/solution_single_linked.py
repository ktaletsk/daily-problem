# Single-linked list
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# Helper function to build inverse list
def create_inverse_list(node):
    # Build inverse single-linked list starting from tail and going back to the head

    # Create the last node of the inverse list -- equal to the first node of the original list
    node_inv = Node(node.val)

    # Continue building the inverse list by linking new elements to the old ones
    while node.next != None:
        # Move 1 step in the original list
        node = node.next

        # Add the new node to the beginning of the inverse list
        next_node_inv = node_inv
        node_inv = Node(node.val)
        node_inv.next = next_node_inv
    return node_inv

def is_palindrome(node):
    # Create the inverse list (Complexity: O(n))
    tail = create_inverse_list(node)
    
    # Iterate through original and iverse lists and check if values are the same all the time (Complexity: O(n))
    while node.next != None:
        # Check that i-th element is equal to (n-i)-th element
        if node.val != tail.val:
            return False

        # Move 1 element along the list
        node = node.next
        tail = tail.next

    # If the end was reached, that means we confirmed palindrome
    return True

# Helper function to build single-linked lists
def build_single_linked_list(values):
    n = len(values)
    result = [Node(value) for value in values]
    for i in range(n-1):
        result[i].next = result[i+1]
        
    return result[0]

# Test the solution
def test():
    assert is_palindrome(build_single_linked_list(['a', 'b', 'b', 'a'])) == True
    assert is_palindrome(build_single_linked_list(['a', 'b', 'c', 'b', 'a'])) == True
    assert is_palindrome(build_single_linked_list(['a', 'a'])) == True
    assert is_palindrome(build_single_linked_list(['a'])) == True
    assert is_palindrome(build_single_linked_list(['a', 'b'])) == False