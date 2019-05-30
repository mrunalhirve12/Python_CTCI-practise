"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
from pip._vendor.msgpack.fallback import xrange


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []

        def getNodes(node):
            if node:
                nodes.append(node)
                if node.left:
                    getNodes(node.left)
                if node.right:
                    getNodes(node.right)

        getNodes(root)

        for i in xrange(len(nodes) - 1):
            node = nodes[i]
            node.right = nodes[i + 1]
            node.left = None
        """
        while root:
            if root.left:
                self.flatten(root.left)
                node1 = root.left
                while node1.right:
                    node1 = node1.right
                node2 = root.right
                root.right = root.left
                root.left = None
                node1.right = node2
            root = root.right
            """

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.flatten(root)
