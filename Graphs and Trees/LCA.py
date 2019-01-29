# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left is not None and findPath(root.left, path, k)) or
            (root.right is not None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False


def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = %d" % (findLCA(root, 4, 5, )))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))
'''


# -------------------------------------------------------------------------------------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    # Base Case
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


# Driver program to test above function

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", findLCA(root, 4, 5).key)
print("LCA(4,6) = ", findLCA(root, 4, 6).key)
print("LCA(3,4) = ", findLCA(root, 3, 4).key)
print("LCA(2,4) = ", findLCA(root, 2, 4).key)
