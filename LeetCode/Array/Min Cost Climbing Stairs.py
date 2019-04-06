"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        # For any step(index) in stairs(cost), we can jump into that step(index) from step - 2 or step -1,
        # start iterating by 2 till end
        for i in range(2, len(cost)):
            # we accumulate costs while considering min every step
            cost[i] += min(cost[i - 1], cost[i -2])
        # return min between last two
        return min(cost[-1], cost[-2])

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))

"""
TestCase #1
s.minCostClimbingStairs([10, 15, 20])

TestCase #2
s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

TestCase #3
s.minCostClimbingStairs([0,0,0,0])
"""
