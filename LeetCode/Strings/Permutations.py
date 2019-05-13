"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # To Do
        stack = [([])]
        res = []

        while stack:
            comb = stack.pop()
            if len(comb) == len(nums):
                res.append(comb)
                continue
            for n in range(0, len(nums)):
                if nums[n] not in comb:
                    stack.append((comb + [nums[n]]))
        return res

s = Solution()
s.permute([1,2,3])