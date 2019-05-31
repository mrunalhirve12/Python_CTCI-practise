"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maximum = 0
        table = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    table[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        table[i][j] = 1
                    else:
                        table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
                if table[i][j] > maximum:
                    maximum = table[i][j]
        return maximum * maximum


mat = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
s = Solution()
s.maximalSquare(mat)
