class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            flag = False
            if self.children == [] and other.children == []:
                flag = self.value == other.value
            else:
                # Get list of children values
                sortedChildren1 = sorted(self.children, key=lambda ch: ch.value)
                sortedChildren2 = sorted(other.children, key=lambda ch: ch.value)

                chv1 = [n.value for n in sortedChildren1]
                chv2 = [n.value for n in sortedChildren2]

                if chv1==chv2:
                    # Children nodes are equal
                    flag = all([child1 == child2 for child1, child2 in zip(sortedChildren1, sortedChildren2)])
            return flag
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def isSymmetric(self):
        if len(self.children) < 2:
            return true
        else:
            return all([i==self.children[0] for i in self.children[1:]])

def main():
    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    print(tree.isSymmetric())
    # True

if __name__== "__main__":
    main()