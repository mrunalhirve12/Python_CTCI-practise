"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            seen[i][j] = 1
            trav = i
            while trav > 0 and maze[trav - 1][j] != 1:
                trav -= 1
            if trav != i and seen[trav][j] != 1:
                if dfs(trav, j):
                    return True
            trav = i
            while trav < len(maze) - 1 and maze[trav + 1][j] != 1:
                trav += 1
            if trav != i and seen[trav][j] != 1:
                if dfs(trav, j):
                    return True
            trav = j
            while trav > 0 and maze[i][trav - 1] != 1:
                trav -= 1
            if trav != j and seen[i][trav] != 1:
                if dfs(i, trav):
                    return True
            trav = j
            while trav < len(maze[0]) - 1 and maze[i][trav + 1] != 1:
                trav += 1
            if trav != j and seen[i][trav] != 1:
                if dfs(i, trav):
                    return True
            return False

        if not maze or not maze[0]:
            return False
        seen = [[0] * len(maze[0]) for _ in range(len(maze))]
        if dfs(start[0], start[1]):
            return True
        return False