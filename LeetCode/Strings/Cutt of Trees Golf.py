"""
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.


You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6


Example 2:

Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1


Example 3:

Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
"""
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # maximum matrix size is 50x50, meaning that at most, trees will be in range [2, 251]
        # but there is no indication that trees are mapped to this range in the input so we'll do it ourselves.
        # afterwards, let int z denote which tree you're looking for, the target.
        # the state for BFS is then uniquely determined by x = row, y = col, z = target
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], [i, j]))
        heapq.heapify(trees)
        height = 2
        while len(trees) > 0:
            tree = heapq.heappop(trees)
            forest[tree[1][0]][tree[1][1]] = height
            height += 1
        finishHeight = height  # when you've seen all trees you should be looking for a tree of height finishHeight

        q = deque()
        q.appendleft([0, 0, 2])
        visited = set()
        visited.add((0, 0, 2))
        moves = 0

        def neighbors(x, y):
            res = []
            if x - 1 >= 0 and forest[x - 1][y] != 0: res.append([x - 1, y])
            if x + 1 < len(forest) and forest[x + 1][y] != 0: res.append([x + 1, y])
            if y - 1 >= 0 and forest[x][y - 1] != 0: res.append([x, y - 1])
            if y + 1 < len(forest[0]) and forest[x][y + 1] != 0: res.append([x, y + 1])
            return res

        while len(q) > 0:
            n = len(q)
            for i in range(n):
                [x, y, z] = q.popleft()
                if forest[x][y] == z: z += 1
                if z == finishHeight: return moves
                for [x2, y2] in neighbors(x, y):
                    if (x2, y2, z) not in visited:
                        visited.add((x2, y2, z))
                        q.append([x2, y2, z])
            moves += 1
        return -1