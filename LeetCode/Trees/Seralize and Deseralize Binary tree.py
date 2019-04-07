"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Accepted
170,489
Submissions
425,901
Seen this question in a real interview before?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def addNode(root):
            if root:
                # append the data of node
                res.append(str(root.val))

                # First recur on left child
                addNode(root.left)

                # now recur on right child
                addNode(root.right)
            else:
                res.append("null")

        res = []
        addNode(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def doit():
            # get next object from iterator, if null then node is none, else create node and iterate to left and right
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        # since list object is not iterator, we use iter to split values
        vals = iter(data.split())
        return doit()


# Your Codec object will be instantiated and called as such:

# Driver program to test above function

# Let us construct the BST shown in the figure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
print(codec.serialize(root))
print(codec.deserialize(codec.serialize(root)))
