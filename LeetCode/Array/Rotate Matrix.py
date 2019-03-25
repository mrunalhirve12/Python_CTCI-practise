"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0 | n != len(matrix[0]):
            return False

        for layer in range(n//2):
            first = layer
            last = n - layer -1

            for i in range(first, last):
                offset = i - first

                # save top
                top = matrix[first][i]

                # left -> top
                matrix[first][i] = matrix[last - offset][first]

                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]

                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]

                # top -> right
                matrix[i][last] = top

        return matrix

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])