"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search_for(nums, target, left=True):
            i = 0
            j = len(nums)
            while i < j:
                mid = (i + j) // 2
                if nums[mid] == target:
                    if left:
                        j = mid
                    else:
                        i = mid + 1
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i

        left = search_for(nums, target, True)
        right = search_for(nums, target, False)
        if not nums:
            return [-1, -1]
        elif 0 <= left < len(nums) and nums[left] == target:
            return [left, right - 1]
        else:
            return [-1, -1]


s = Solution()
s.searchRange([5,7,7,8,8,10],8)