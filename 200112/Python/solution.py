class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    level = [root]
    while level != []:
        next_level = []
        for el in level:
            print(el.val)
            if el.left != None:
                next_level.append(el.left)
            if el.right != None:
                next_level.append(el.right)
        level = next_level

def test_1():
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    assert print_level_order(root) == [1,2,3,4,5]

def test_2():
    root = Node(7, Node(4), Node(1, Node(9), Node(0)))
    assert print_level_order(root) == [7,4,1,9,0]

def test_3():
    root = Node(1)
    assert print_level_order(root) == [1]