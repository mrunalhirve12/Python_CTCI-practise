"""
Implement an obj over a binary search tree (BST). Your obj will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTobj obj = new BSTobj(root);
obj.next();    // return 3
obj.next();    // return 7
obj.hasNext(); // return true
obj.next();    // return 9
obj.hasNext(); // return true
obj.next();    // return 15
obj.hasNext(); // return true
obj.next();    // return 20
obj.hasNext(); // return false

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""


# Definition for a binary tree node.
# since we want O(h) as space complexity; append only left nodes
# in has next while popping check if root has right node and append all its left first
# it will append the element at at last so this will be latest node popping out
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        while root:
            self.nodes.append(root)
            root = root.left

    def hasNext(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return len(self.nodes) > 0

    def next(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        ret = self.nodes.pop()
        cur = ret.right
        while cur:
            self.nodes.append(cur)
            cur = cur.left
        return ret.val


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Your BSTobj object will be instantiated and called as such:
obj = BSTIterator(root)
x = obj.next()
x = obj.next()
x = obj.hasNext()
x = obj.next()
x = obj.hasNext()
x = obj.next()
x = obj.hasNext()
x = obj.next()
x = obj.hasNext()
