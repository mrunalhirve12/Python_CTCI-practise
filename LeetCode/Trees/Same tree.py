"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Iterative to do
        queue = collections.deque([p, q])
        while queue:
            u1 = queue.popleft()
            u2 = queue.popleft()
            if u1 == None and u2 != None:
                return False
            if u1 != None and u2 == None:
                return False
            if u1 != None and u2 != None:
                if u1.val != u2.val:
                    return False
                else:
                    queue.append(u1.left)
                    queue.append(u2.left)
                    queue.append(u1.right)
                    queue.append(u2.right)
        return True
        """
        # RECURSIVE
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        """


l1 = TreeNode(3)
l1.left = TreeNode(5)
l1.right = TreeNode(1)

l2 = TreeNode(3)
l2.left = TreeNode(5)
l2.right = TreeNode(1)

s = Solution()
s.isSameTree(l1, l2)
