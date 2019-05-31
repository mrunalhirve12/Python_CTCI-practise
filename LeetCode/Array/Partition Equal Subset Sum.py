"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
"""


class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        nums.sort()
        for num in nums:
            if num == target:
                return True
            if num > target:
                return False

        memo = [False] * (target + 1)
        memo[0] = True

        for i in range(len(nums)):
            level = memo[:]
            for j in range(len(memo)):
                if memo[j] and (j + nums[i]) < len(memo):
                    level[j + nums[i]] = True
            memo = level

        return memo[-1]

s = Solution()
s.canPartition([1, 2, 3, 5, 1])