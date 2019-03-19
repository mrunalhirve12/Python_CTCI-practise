"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #check if num is empty or None
        if nums is None or not nums:
            return None
        #sort the array
        nums = sorted(nums)
        #using set to store unique
        result = set()
        #iterate
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                #here check if there is any other set possible with num [i]
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        #returns list of results
        return list(result)

s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -4])

"""
TestCase #1
s = Solution()
s.threeSum( [-1, 0, 1, 2, -1, -4])

TestCase #2
s = Solution()
s.threeSum( [])

TestCase #3
s = Solution()
s.threeSum()

TestCase #4
s = Solution()
s.threeSum( [])
"""