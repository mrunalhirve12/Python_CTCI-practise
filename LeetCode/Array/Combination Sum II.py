p-"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # TO DO
        def helper(j, target):
            if target <= 0 or not candidates or j < 0:
                return []
            res = []
            for i in range(j, -1, -1):
                if candidates[i] > target:
                    continue
                elif i <= j - 1 and candidates[i] == candidates[i + 1]:  # avoid duplicates
                    continue
                elif candidates[i] == target:
                    res.append([candidates[i]])
                else:
                    tmp = helper(i - 1, target - candidates[i])
                    res += [lst + [candidates[i]] for lst in tmp]
            return res

        candidates = sorted(candidates)
        res = helper(len(candidates) - 1, target)
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))