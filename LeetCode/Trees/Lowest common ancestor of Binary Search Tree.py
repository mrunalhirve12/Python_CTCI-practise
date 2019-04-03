"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Function to find LCA of n1 and n2. The function assumes
        # that both n1 and n2 are present in BST
        """
        #RECURSIVE SOLUTION
        # Base Case
        if not root or not p or not q:
            return None
        #chk if max of two vals is less /greater than present root(bst) else return root
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root.val
        """

        #ITERATIVE SOLUTION
        # Base Case
        if not root or not p or not q:
            return None
        #iterative
        while root:
            if root.val > q.val and root.val > p.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right
            else:
                return root.val


# Driver program to test above function

# Let us construct the BST shown in the figure
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


s = Solution()

n1 = TreeNode(2)
n2 = TreeNode(8)
print(s.lowestCommonAncestor(root, n1, n2))

n1 = TreeNode(7)
n2 = TreeNode(9)
print(s.lowestCommonAncestor(root, n1, n2))