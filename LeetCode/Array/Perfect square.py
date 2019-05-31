"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        for i in xrange(1, int(n ** 0.5) + 1):
            dp[i ** 2] = 1

        for i in xrange(1, n + 1):
            for k in xrange(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - k ** 2] + 1)

        return dp[n]


s = Solution()
print(s.numSquares(12))