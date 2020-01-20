class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(node):
    level = 0
    current_level = [node]
    min_sum = sum([n.val for n in current_level])
    min_level = 0
    
    # Traverse the tree in the breadth-first manner
    while current_level != []:
        s = sum([n.val for n in current_level])
        if s < min_sum:
            min_sum = s
            min_level = level
        
        # Get the next layer of the tree by extracting children of the current level
        next_level = []
        for n in current_level:
            if n.left != None:
                next_level.append(n.left)
            if n.right != None:
                next_level.append(n.right)
        current_level = next_level
        level += 1

    return min_level

def test_1():
    #     10
    #    /  \
    #   2    8
    #  / \    \
    # 4   1    2
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)
    
    assert minimum_level_sum(node)==2

def test_2():
    #      5 
    #    /   \
    #   1     3
    #  / \   / \
    # 7   1 2   2
    node = Node(5)
    node.left = Node(1)
    node.right = Node(3)
    node.left.left = Node(7)
    node.left.right = Node(1)
    node.right.left = Node(2)
    node.right.right = Node(2)
    
    assert minimum_level_sum(node)==1