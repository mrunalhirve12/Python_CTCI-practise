"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #initialize two pointers
        left = 0
        right = len(height) - 1
        #initiliaze max variable
        left_max = right_max = water = 0
        #iterate through left is smaller than right
        while left <= right:
            #Compare left_max and right_max
            if left_max <= right_max:
                #if left_max is smaller than right_max;
                #calculate left_max and count water
                #keep moving left
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                # if right_max is smaller than left_max;
                # calculate right_max and count water
                # keep moving right
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])