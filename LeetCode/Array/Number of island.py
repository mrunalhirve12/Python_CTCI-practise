"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        # RECURSIVE SOLUTION : The problem can be solved with DFS. Time complexity: O(height * width), space complexity: O(height * width).
        def dfs(grid, u):
            # get the index position from tuple
            i, j = u[0], u[1]
            # add tuple to visited set
            visit.add((i, j))
            # if i > 0 check row above having val as 1 and not visited
            if i > 0 and grid[i-1][j] == 1 and (i-1, j) not in visit:
                dfs(grid, (i-1, j)) # check recursively
            # if i < ht (all cases) check below above having val as 1 and not visited
            if i < height - 1 and grid[i+1][j] == 1 and (i+1, j) not in visit:
                dfs(grid, (i+1, j))
            # if j > 0 check  previous col in same row having val as 1 and not visited
            if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in visit:
                dfs(grid, (i, j - 1)) # check recursively
            # if j < width check  previous col in same row having val as 1 and not visited
            if j < width - 1 and grid[i][j + 1] == 1 and (i, j + 1) not in visit:
                dfs(grid, (i, j+1))

        # calculate length of grid
        if len(grid) == 0:
            return 0
        # count to store clusters
        count = 0
        # a set to maintain visited
        visit = set()
        # calculate height and width of the grid
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i,j) not in visit:
                    dfs(grid, (i,j))
                    count += 1
        return count
        """

        # ITERATIVE SOLUTION
        if len(grid) == 0:
            return 0
            # count to store clusters
        count = 0
        # a set to maintain visited
        visit = set()
        # calculate height and width of the grid
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i, j) not in visit:
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        u = stack.pop()
                        visit.add(u)
                        h, w = u[0], u[1]
                        # if h > 0 check row above having val as 1 and not visited
                        if h > 0 and grid[h - 1][w] == 1 and (h - 1, w) not in visit:
                            stack.append((h - 1, w))
                        # if i < ht (all cases) check below above having val as 1 and not visited
                        if h < height - 1 and grid[h + 1][w] == 1 and (h + 1, w) not in visit:
                            stack.append((h + 1, w))
                        # if j > 0 check  previous col in same row having val as 1 and not visited
                        if w > 0 and grid[h][w - 1] == 1 and (h, w - 1) not in visit:
                            stack.append((h, w-1))
                        # if j < width check  previous col in same row having val as 1 and not visited
                        if w < width - 1 and grid[h][w + 1] == 1 and (h, w + 1) not in visit:
                            stack.append((h, w + 1))
        return count




mat = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
s = Solution()
print(s.numIslands(mat))
