"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        for line in range(1, numRows):
            c = 1
            for i in range(1, line+1):
                print(c)
                c = int(c * (line-i) / i)
            print("")

s = Solution()
s.generate(4)