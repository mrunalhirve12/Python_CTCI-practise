"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collector = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):  # use enumerate instead
            if c in collector and collector[c] >= start:
                start = collector[c] + 1
            else:
                ans = max(ans, i - start + 1)
            collector[c] = i
        return ans

s = Solution()
s.lengthOfLongestSubstring("abcabc")
