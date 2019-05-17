"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        # FAILS Test 2
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return nums
        """

        i = 0
        k = len(nums) - 1
        j = i
        while j <= k:
            # fails for test 2
            #if nums[i] > nums[j]:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        return nums

s = Solution()
print(s.sortColors([0,1,2,0,1,2]))

"""
TESTCASE #1
print(s.sortColors([2,0,2,1,1,0]))

TESTCASE #2
print(s.sortColors([2,0,1]))

TESTCASE #3
print(s.sortColors([0,1,0]))

"""