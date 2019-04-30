"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_hash = set(nums)
        ans = 0
        for num in nums:
            # main for time limit
            if num + 1 in nums_hash:
                continue
            count = 0
            while num in nums_hash:
                count += 1
                num = num - 1
            ans = max(ans, count)
        return ans


s = Solution()
s.longestConsecutive([100, 4, 200, 1, 3, 2])
