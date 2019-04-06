# Definition for a binary tree node.
import queue
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if root is None
        if root is None:
            return []
        # initialize final result list res, queue.
        res = []
        queue = []
        # append root in queue
        queue.append(root)
        # while queue not empty
        while queue:
            # take values from queue of each level as list
            res.append([c.val for c in queue])
            # initialize new list
            qq = []
            # for nodes in queue each level, get it left and right child
            for node in queue:
                if node.left is not None:
                    qq.append(node.left)
                if node.right is not None:
                    qq.append(node.right)
            # append new list in queue
            queue = qq
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.levelOrder(root)

"""
Test Case #1
s.levelOrder([])
"""

