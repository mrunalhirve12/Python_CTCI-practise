class LinkedList:
    next = None
    val = None

    def __init__(self, val):
        self.val = val

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val}) ".format(val=self.val) + str(self.next)


class BinaryTree:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "<Binary Tree (val is {val}). \n\tleft is {left} \n\tright is {right}>".format(val=self.val,
                                                                                              left=self.left,
                                                                                              right=self.right)


def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight


def tree_to_linked_lists(tree, lists={}, d=None):
    if d == None:
        d = depth(tree)
    if lists.get(d) == None:
        lists[d] = LinkedList(tree.val)
    else:
        lists[d].add(tree.val)
        if d == 1:
            return lists
    if tree.left != None:
        lists = tree_to_linked_lists(tree.left, lists, d - 1)
    if tree.right != None:
        lists = tree_to_linked_lists(tree.right, lists, d - 1)
    return lists


if __name__ == '__main__':
    mainTree = BinaryTree(1)
    someSubTrees = {"left": BinaryTree(2), "right": BinaryTree(3)}
    someSubTrees["left"].left = BinaryTree(4)
    someSubTrees["left"].right = BinaryTree(5)
    someSubTrees["right"].left = BinaryTree(6)
    someSubTrees["right"].right = BinaryTree(7)
    someSubTrees["right"].right.right = BinaryTree(8)
    someSubTrees["left"].left.left = BinaryTree(9)
    mainTree.left = someSubTrees["left"]
    mainTree.right = someSubTrees["right"]
    ttll = tree_to_linked_lists(mainTree)
    for depthLevel, linkedList in ttll.items():
        print("{0} {1}".format(depthLevel, linkedList))

