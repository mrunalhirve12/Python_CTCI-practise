"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        #FAILS for [3,2,4,1], as does not considers previous numbers
        res = [[]]
        for i in range(len(nums)):
            res.append([nums[i]])
            j = len(nums)-1
            while i < j:
                res.append([nums[i], nums[j]])
                if ([nums[i]] + nums[j:]) not in res:
                    res.append([nums[i]] + nums[j:])
                j -= 1
        print(res)

        """
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        print(res)


s = Solution()
s.subsets([3,2,4,1])

"""
s= Solution
#Test Case 1
s.subsets([1,2,3])

#Test Case 2
s.subsets([0])

#Test Case 3
s.subsets([])

#Test Case 4
s.subsets([3,2,4,1])
"""
