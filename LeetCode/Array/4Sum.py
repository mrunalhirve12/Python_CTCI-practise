"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # idea to use same technique of incrementing and decrementing pointers
        a = sorted(nums)
        res = set()
        n = len(a)
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                rem = target - (a[i] + a[j])
                left, right = j+1, n-1
                while left < right:
                    if a[left] + a[right] == rem:
                        # to add tuple to res
                        res.add(tuple([a[i], a[j], a[left], a[right]]))
                        left = left + 1
                    elif a[left] + a[right] < rem:
                        left = left + 1
                    else:
                        right = right - 1
        # sorted converts set to list
        return sorted([list(x) for x in res])


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))