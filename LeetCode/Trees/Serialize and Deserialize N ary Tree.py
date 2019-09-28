# Definition for a Node.

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Codec:

    def serialize(self, root):
        Encodes a tree to a single string.

        #type root: Node
        #rtype: str


        def dfs(root):
            if not root:
                return
            res.append(str(root.val) + "[")
            for child in root.children:
                if child:
                    dfs(child)
            res.append("]")

        res = []
        dfs(root)
        return "".join(res)

    def deserialize(self, data):
        #Decodes your encoded data to tree.

        #type data: str
        #rtype: Node

        data = data.split("]")
        data.pop()  # pop the extra "" at the end
        head = None
        stack = []
        for string in data:
            chars = string.split("[")
            for char in chars:
                if char != "":
                    if not head:
                        head = Node(int(char), [])
                        stack.append(head)
                    else:
                        node = Node(int(char), [])
                        stack[-1].children.append(node)
                        stack.append(node)
            stack.pop()
        return head
"""

def test():
    data = '1[3[5[],6[]],2[],4[]]'
    data = data.split(']')
    print(data)
    data.pop()
    print(data)
    head = None
    stack = []
    for string in data:
        chars = string.split("[")
        print(chars)
        for char in chars:
            if char != "":
                if not head:
                    head = Node(int(char), [])
                    stack.append(head)
                else:
                    node = Node(int(char), [])
                    stack[-1].children.append(node)
                    stack.append(node)
        stack.pop()
    return head

test()