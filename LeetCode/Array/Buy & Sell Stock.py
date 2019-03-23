"""
121. Best Time to Buy and Sell Stock
Easy

2294

114

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min = sys.maxsize
        maxprofit = -sys.maxsize-1
        for i in range(len(prices)):
            if prices[i] < min  :
                min = prices[i]
            if prices[i] - min > maxprofit:
                maxprofit = prices[i] - min
        print(maxprofit)
        return maxprofit


s = Solution()
s.maxProfit([])

"""
Test Case #1
s.maxProfit( [7,6,4,3,1])

Test Case #2
s.maxProfit([7,1,5,3,6,4])

Test Case #3
s.maxProfit([])

Test Case #3
s.maxProfit("caba")
"""