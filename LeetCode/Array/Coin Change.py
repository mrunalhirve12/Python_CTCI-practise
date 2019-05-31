"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""
from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rs = [amount + 1] * (amount + 1)
        rs[0] = 0
        for i in xrange(1, amount + 1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i - c] + 1)

        if rs[amount] == amount + 1:
            return -1
        return rs[amount]

s = Solution()
s.coinChange([1, 2, 5], 11)