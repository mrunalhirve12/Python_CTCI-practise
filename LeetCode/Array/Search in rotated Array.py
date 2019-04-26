"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # calculate l and r
        l = 0
        r = len(nums) - 1
        # iterate till left is less than right
        while l <= r:
            # keep calculating mid and also check mid, left and right elements
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            # if the element not found at corners and mid;
            # if target is smaller than left; move the left index by 1 ; else move right index by 1
            else:
                if nums[l] > target:
                    l = l + 1
                else:
                    r = r - 1
        return -1



s = Solution()
print(s.search([1,3], 3))

"""
TestCase #1
print(s.search([4,5,6,7,0,1,2], 6))

TestCase #2
print(s.search([4,5,6,7,0,1,2], 6))

TestCase #3
print(s.search([4,5,6,7,0,1,2], 6))

TestCase #4
print(s.search([], 5))

TestCase #5
print(s.search([1,3], 5))
"""