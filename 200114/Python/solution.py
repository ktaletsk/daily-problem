class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val

def lowestCommonAncestor(root, a, b):
    ancestry_a = []
    pointer_a = a
    while pointer_a != None:
        ancestry_a.append(pointer_a)
        pointer_a = pointer_a.parent


    ancestry_b = []
    pointer_b = b
    while pointer_b != None:
        ancestry_b.append(pointer_b)
        pointer_b = pointer_b.parent

    # Find common ancestor
    it = -1
    while -it <= len(ancestry_a) and -it <= len(ancestry_b):
        if ancestry_a[it] != ancestry_b[it]:
            break
        it -= 1
        
    return ancestry_a[it+1]

def test_1():
    #   a
    #  / \
    # b   c
    #    / \
    #   d*  e*
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    b = root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    assert lowestCommonAncestor(root, a, b).val == 'c'

def test_2():
    #   a
    #  / \
    # b*  c
    #    / \
    #   d*  e
    root = TreeNode('a')
    b = root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    assert lowestCommonAncestor(root, a, b).val == 'a'

def test_3():
    #   a
    #  / \
    # b   c*
    #    / \
    #   d*  e
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    b = root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    assert lowestCommonAncestor(root, a, b).val == 'c'