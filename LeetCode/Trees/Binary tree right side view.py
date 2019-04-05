"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # res list
        res = []
        # call the dfs function with parameters as root, length of tree and res array
        self.dfs(root, 0, res)
        # return res
        return res

    def dfs(self, root, level, res):
        # if not root return empty
        if not root:
            return
        # here we only append if the level and res same, so first node (since we call right  subtree first) it gets appended
        if len(res) == level:
            res.append(root.val)

        # call the right & left subtree first, increment levels using recursion
        self.dfs(root.right, level + 1, res)
        self.dfs(root.left, level + 1, res)

# Driver program to test above function

# Let us construct the BST shown in the figure
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)

s = Solution()
print(s.rightSideView(root))
