"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #if no field
        if not matrix or target is None:
            return False

        #calculate rows and cols
        rows, cols = len(matrix), len(matrix[0])

        #calculate lows and highs
        low, high = 0, rows*cols -1

        while low <= high:
            mid = int(low + high)/2
            #calculating the no index of array.
            num = matrix[int(mid/cols)][int(mid%cols)]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

"""
O(log(M)) + O(log(N)) Solution

Use binary search to select the right row. Then use binary search to search within a column,
class Solution(object):
    # O(log(M)) + O(log(N))
    def bsearch(self, nums, low, high, target):
        while low <= high:
            mid = low + int((high-low)/2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return False
    
    def searchMatrix(self, matrix, target):
    
        #type matrix: List[List[int]]
        #type target: int
        #rtype: bool
        
        M,N = len(matrix), len(matrix[0])
        low, high = 0, M-1
        while low <= high:
            mid = low + (high-low)//2
            if matrix[mid][0] <= target <= matrix[mid][N-1]:
                return self.bsearch(matrix[mid], 0, N-1, target)
            elif target > matrix[mid][N-1]:
                low = mid+1
            elif target < matrix[mid][0]:
                high = mid-1            
        return False
    """


mat = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]

s = Solution()
s.searchMatrix(mat, 3)