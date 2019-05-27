import sys

class Node:
    def _init_(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def isValid(lot, visited, M, N, row, col):
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) and not lot[row][col] == 0 and not visited[row][col]


def removeObstacle(numRows, numColumns, lot):
    if numRows < 1 or numColumns > 1000 or numColumns < 1:
        return -1

    for i in range(len(lot)):
        for j in range(len(lot[0])):
            if lot[i][j] == 9:
                x = i
                y = j
                print("x, y", x, y)
                break

    visited = [[False for i in range(numColumns)] for j in range(numRows)]
    queue = []
    # for src
    visited[0][0] = True

    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    queue.append(Node(0, 0, 0))

    # mark source cell as visited and enqueue the source node

    min_dist = sys.maxsize

    while queue:
        node = queue.pop(0)
        print("x,y, dist", node.x, node.y, node.dist)
        i = node.x
        j = node.y
        dist = node.dist

        if i == x and j == y:
            print("x, y", x, y)
            print("i,j", i, j)
            min_dist = dist
            break

        for k in range(4):

            if (isValid(lot, visited, numRows, numColumns, i + row[k], j + col[k])):
                visited[i + row[k]][j + col[k]] = True
                queue.append(Node.__new__((i + row[k]), (j + col[k]), (dist + 1)))

    return min_dist

"""
print('##### Edge cases ######')
print('Output: ', removeObstacle(1, 1, [[9]]))
print('Output: ', removeObstacle(0, 0, [[]]))

print('\n##### Input: 1 ######')
m = 3
n = 3
l = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 9, 1]
]
print('Output: ', removeObstacle(m, n, l))

print('\n##### Input: 2 ######')
m = 5
n = 4
l = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 9, 1],
    [0, 0, 1, 1]
]
print('Output: ', removeObstacle(m, n, l))
"""
print('\n##### Input: 3 ######')
m = 5
n = 4
l = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 9]
]
print('Output: ', removeObstacle(m, n, l))
