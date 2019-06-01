#572. Subtree of Another Tree
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(s, t):
            if s == None and t == None:
                return True
            elif s == None or t == None:
                return False
            l = check(s.left, t.left)
            r = check(s.right, t.right)
            if s.val == t.val and l and r:
                return True
            return False

        if check(s, t): return True
        if s.left and self.isSubtree(s.left, t): return True
        if s.right and self.isSubtree(s.right, t): return True
        return False