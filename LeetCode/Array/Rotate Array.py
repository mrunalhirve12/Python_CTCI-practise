"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        print(nums)
        """

        #RETURNS PREVIOUS NUMS???
        #nums = list(nums)
        for i in range(k):
            val = nums.pop()
            nums = [val] + nums
        print(nums)
        return nums



        """
        #NAIVE APPROACH O(N) EXTRA SPACE
        x = []
        x = nums
        for i in range(k):
            val = x.pop()
            x = [val] + x
        print(x)
        """

s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))