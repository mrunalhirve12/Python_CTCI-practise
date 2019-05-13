"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Same as spiral matrix; no difference
        y0 = 0
        y1 = n
        x0 = 0
        x1 = n
        res = [[0] * n for _ in range(n)]
        count = 1
        while y0 < y1 and x0 < x1:
            for i in range(x0, x1):
                res[y0][i] = count
                count += 1
            for j in range(y0 + 1, y1 - 1):
                res[j][x1 - 1] = count
                count += 1
            if y1 - 1 != y0:
                for i in range(x1 - 1, x0 - 1, -1):
                    res[y1 - 1][i] = count
                    count += 1
            if x0 != x1 - 1:
                for j in range(y1 - 2, y0, -1):
                    res[j][x0] = count
                    count += 1
            y0 += 1
            y1 -= 1
            x0 += 1
            x1 -= 1
        return res

s = Solution()
print(s.generateMatrix(3))