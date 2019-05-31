"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
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
        def to_string(node, q):
            if not node:
                q.append("#")
            else:
                q.append(str(node.val))
                to_string(node.left, q)
                to_string(node.right, q)

        q = []
        to_string(root, q)
        return ",".join(q)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def to_tree(nodes):
            if not nodes:
                return None
            val = nodes.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = to_tree(nodes)
            node.right = to_tree(nodes)
            return node

        return to_tree(data.split(","))


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.serialize(root))
print(codec.deserialize(codec.serialize(root)))