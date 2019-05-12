#https://leetcode.com/problems/next-permutation/discuss/241684/concise-python-solution-beat-99

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i
                while j < n and nums[j] > nums[i - 1]:
                    idx = j
                    j += 1
                nums[idx], nums[i - 1] = nums[i - 1], nums[idx]
                # for case #2
                for k in range((n - i) // 2):
                    nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]
                # if not break will go to reverse
                break
        else:
            nums.reverse()


s = Solution()
print(s.nextPermutation([1,3,2]))

"""
TESTCASE #1
print(s.nextPermutation([1,2,3]))

TESTCASE #2
print(s.nextPermutation([1,3,2]))

TESTCASE #3
print(s.nextPermutation([3,2,1]))

"""