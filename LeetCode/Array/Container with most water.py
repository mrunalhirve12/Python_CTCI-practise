"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # idea is to take a height and calculate water always
        # Find the max water from this
        max = -9999
        n = len(height)
        i = 0
        k = n - 1
        while i < k :
            container = k - i
            if height[i] < height[k]:
                multiplier = height[i]
                i += 1
            else:
                multiplier = height[k]
                k -= 1
            water = container * multiplier
            if water > max:
                max = water
        return max

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))