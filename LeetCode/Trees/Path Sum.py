"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        """
        # Recursive
        if not root:
            return False
        elif not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        """
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            u = stack.pop()
            if not u[0].left and not u[0].right:
                if u[1] == 0:
                    return True
            if u[0].left:
                stack.append((u[0].left, u[1] - u[0].left.val))
            if u[0].right:
                stack.append((u[0].right, u[1] - u[0].right.val))
        return False

l1 = TreeNode(5)
l1.left = TreeNode(4)
l1.right = TreeNode(8)
l1.left.right = TreeNode(11)
l1.left.right.right = TreeNode(2)
l1.left.right.left = TreeNode(7)
l1.right.left = TreeNode(13)
l1.right.right = TreeNode(4)
l1.right.right.left = TreeNode(1)

s = Solution()
s.hasPathSum(l1, 22)