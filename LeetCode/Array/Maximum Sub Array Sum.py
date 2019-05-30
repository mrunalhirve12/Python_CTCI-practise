"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""
from pip._vendor.msgpack.fallback import xrange

"""
class Solution(object):
    def maxSubArray(self, nums):
        
        :type nums: List[int]
        :rtype: int
        # To Do
        largest_end_here = nums[0]
        largest_til_here = nums[0]
        for i in range(1, len(nums)):
            if largest_end_here + nums[i] < nums[i]:
                largest_end_here = nums[i]
            else:
                largest_end_here += nums[i]
            if largest_til_here < largest_end_here:
                largest_til_here = largest_end_here
        return largest_til_here
"""
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return None
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])