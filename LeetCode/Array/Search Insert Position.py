"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # idea is simple just check if no is smaller than element at ith index
        # else return len of elements
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if i == 0 and target < nums[i]:
                return 0
            if i != 0 and target < nums[i]:
                return i
        return len(nums)

s = Solution()
print(s.searchInsert([1,3,5,6], 0))
"""
TESTCASE #1
print(s.searchInsert([1, 3, 5, 6], 5))

TESTCASE #2
print(s.searchInsert([1,3,5,6], 2))

TESTCASE #3
print(s.searchInsert([1,3,5,6], 7))

TESTCASE #4
print(s.searchInsert([1,3,5,6], 0))
"""

