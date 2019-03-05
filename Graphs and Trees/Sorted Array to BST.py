#https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
    if not arr:
        return None

    # find middle
    mid = int((len(arr)) / 2)

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root


# A utility function to print the preorder
# traversal of the BST
def preOrder(node):
    if not node:
        return

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


# driver program to test above function
""" 
Constructed balanced BST is  
    4 
/ \ 
2 6 
/ \ / \ 
1 3 5 7 
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8]
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST")
preOrder(root)