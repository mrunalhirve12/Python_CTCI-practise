"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        s1_rl, s2_lr = [root], []
        output, rl = [], True
        while s1_rl or s2_lr:
            op = []
            if rl:
                for _ in range(len(s1_rl)):
                    x = s1_rl.pop()
                    op.append(x.val)
                    if x.left:
                        s2_lr.append(x.left)
                    if x.right:
                        s2_lr.append(x.right)
            else:
                for _ in range(len(s2_lr)):
                    x = s2_lr.pop()
                    op.append(x.val)
                    if x.right:
                        s1_rl.append(x.right)
                    if x.left:
                        s1_rl.append(x.left)
            rl = not rl
            output.append(op)
        return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.zigzagLevelOrder(root))