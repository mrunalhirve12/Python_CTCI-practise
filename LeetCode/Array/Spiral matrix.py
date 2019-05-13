#https://leetcode.com/problems/spiral-matrix/discuss/244270/Python-beat-100
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        y0 = 0
        y1 = len(matrix)
        x0 = 0
        x1 = len(matrix[0])
        while y1 > y0 and x1 > x0:
            for i in range(x0,x1):
                res.append(matrix[y0][i])
            for j in range(y0+1, y1-1):
                res.append(matrix[j][x1-1])
            if y1 != y0+1:
                for i in range(x1 - 1, x0 - 1, -1):
                    res.append(matrix[y1 - 1][i])
            if x0 != x1 - 1:
                for j in range(y1 - 2, y0, -1):
                    res.append(matrix[j][x0])
            y0 += 1
            y1 -= 1
            x0 += 1
            x1 -= 1
        return res

s = Solution()
s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])