#Leetcode 153
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        # if the leftmost element is smaller than right i.e the left is smallest element
        if nums[l] <= nums[r]:
            return nums[l]
        # now keep checking till left is smaller than equal to righ
        while l <= r:
            # calculate mid
            mid = (l + r) // 2
            # if mid is greater than mid + 1; mid + 1 is always smaller element
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            else:
                # else keep decreasing size of the array;
                # if left is greater than mid there are chances the min is in left
                # else min will be at right
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return nums[l]

s = Solution()
print(s.findMin([5,1,2,3,4]))

"""
TestCase : #1


TestCase :#2

TestCase: #3
print(s.findMin([3,1,2]))

TestCase: #4
print(s.findMin([4,5,1,2,3]))

TestCase: #5
print(s.findMin([4,5,1,2,3]))
"""
