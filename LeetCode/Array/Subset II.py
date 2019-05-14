"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
import collections


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # similar to combinarion of phone no easy to
        if not nums:
            return [[]]
        res = [[]]
        dic = collections.Counter(nums)
        for key, val in dic.items():
            tmp = []
            for lst in res:
                for i in range(1, val + 1):
                    tmp.append(lst + [key] * i)
            res += tmp
        return res
s = Solution()
print(s.subsetsWithDup([1,2,2]))