"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_Len = len(matrix)
        if row_Len == 0:
            return False
        col_len = len(matrix[0])
        if col_len == 0:
            return False
        # Starting with the bottom left corner of the matrix,
        row = row_Len - 1
        col = 0
        while col < col_len and row >= 0:
            # if the current element curr equals target, we return True
            if matrix[row][col] == target:
                return True
            # By the same token, if curr is smaller than target, we increase the column index by 1 (move right by 1 column)
            elif matrix[row][col] < target:
                col += 1
            # If curr is larger than target, than since any element to the right of curr (in the same row) is larger than curr,
            # we don't need to consider them, so we deduct the row index by 1 (move up by 1 row)
            else:
                row -= 1
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

s = Solution()
s.searchMatrix(matrix, 5)
