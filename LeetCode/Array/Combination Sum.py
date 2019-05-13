"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # TO DO
        def helper(candidates, target):
            if not candidates or target <= 0:
                return []
            res = []
            for i in range(len(candidates) - 1, -1, -1):
                if i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    continue
                elif candidates[i] == target:
                    res.append([target])
                tmp = helper(candidates[:i + 1], target - candidates[i])
                res += [lst + [candidates[i]] for lst in tmp]
            return res

        candidates = sorted(candidates)
        return helper(candidates, target)

s = Solution()
s.combinationSum( [2,3,6,7],7)