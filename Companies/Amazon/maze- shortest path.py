#https://medium.com/@codingfreak/maze-problems-in-data-structures-8530af4d6c8

# from given source to given destination
import sys


def shortestpath(mat):

    def isValid(x, y):
        if row_len > x >= 0 and col_len > y >= 0:
            return True
        else:
            return False

    def isSafe(mat, visited, x, y):
        if mat[x][y] == 0 or visited[x][y] != 0:
            return False
        else:
            return True

    def findshortestpath(mat, visited, i, j, x, y, min_dist, dist):

        if i == x and j == y:
            return min(min_dist, dist)

        visited[i][j] = 1

        # bottom cell
        if isValid(i+1, j) and isSafe(mat, visited, i+1, j):
            min_dist = findshortestpath(mat, visited, i+1, j, x, y, min_dist, dist+1)

        # right cell
        if isValid(i, j+1) and isSafe(mat, visited, i, j+1):
            min_dist = findshortestpath(mat, visited, i, j+1, x, y, min_dist, dist+1)

        # top cell
        if isValid(i-1, j) and isSafe(mat, visited, i-1, j):
            min_dist = findshortestpath(mat, visited, i-1, j, x, y, min_dist, dist+1)

        # left cell
        if isValid(i, j-1) and isSafe(mat, visited, i, j-1):
            min_dist = findshortestpath(mat, visited, i, j-1, x, y, min_dist, dist+1)

        visited[i][j] = 0

        return min_dist

    row_len= len(mat)
    col_len = len(mat[0])
    visited = [[0 for _ in range(col_len)] for _ in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            if mat[i][j] == 9:
                dr = i
                dc = j
                break

    min_dist = findshortestpath(mat, visited, 0, 0, dr, dc, sys.maxsize, 0 )
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1

"""
#TESTCASE #1
mat = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]

#TESTCASE #2
mat = [[1, 0, 0], [1, 0, 0], [1, 1, 1]]

#TESTCASE #3
mat = [[1, 0, 0], [1, 0, 0], [0, 9, 1]]

#TESTCASE #4
mat = [[0, 0, 0], [0, 0, 0], [1, 9, 1]]

#TESTCASE #5
mat = [[0, 0, 0], [0, 0, 0], [1, 9, 1]]

"""
mat = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]
print(shortestpath(mat))
