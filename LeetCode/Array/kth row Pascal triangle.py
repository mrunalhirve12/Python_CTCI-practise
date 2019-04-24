"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""
from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        k = 0
        # create a final data structure
        currRow = []
        # iterate through the Rows you want
        while k < numRows + 1:
            # create a new data structure
            nextRow = []
            # iterate through index on each row
            for pos in xrange(k + 1):
                # as last elements are always 1
                if pos == 0 or pos == k:
                    nextRow.append(1)
                # middle elements are addition of prev element rows
                else:
                    nextRow.append(currRow[pos - 1] + currRow[pos])
            # when row is completed add to curr row
            currRow = nextRow
            k += 1

        return currRow

s = Solution()
s.generate(4)