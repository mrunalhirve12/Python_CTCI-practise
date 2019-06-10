"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from pip._vendor.msgpack.fallback import xrange

class Solution(object):
    #Time complexity: O(n**3), where n = len(s), because there are two nested for loops, and the slicing s[j:i] costs an extra O(n). Space complexity: O(n).
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict or not s:
            return False
        dp = [False] * (len(s) + 1)
        #We let dp[0] = True, because the empty string can be segmented into words in wordSet (trivially)
        dp[0] = True
        #iterate through all lengths of string
        for i in xrange(1, len(s) + 1):
            #look for all slices of string if present in dict and mark True
            for j in xrange(i):
                bh = s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        #if all words present return end of the matrix
        return dp[-1]

s = Solution()
s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

"""
TESTCASE #1
s = "leetcode", wordDict = ["leet", "code"]

TESTCASE #2
s = "applepenapple", wordDict = ["apple", "pen"]
 
TESTCASE #3
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
"""