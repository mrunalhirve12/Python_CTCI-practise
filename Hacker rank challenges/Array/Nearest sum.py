import sys


def closest_subtring(intList, n):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = right_max = water = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water



closest_subtring([3,4,5,6,7],14)

