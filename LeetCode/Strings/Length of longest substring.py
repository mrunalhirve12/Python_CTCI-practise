"""
3. Longest Substring Without Repeating Characters
Medium

5051

266

Favorite

Share
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
import sys


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {};
        maxLen = resStart = 0;
        for i, ch in enumerate(s):
            if ch in dic:
                maxLen = max(maxLen, i - resStart);
                resStart = max(resStart, dic[ch] + 1);
            dic[s[i]] = i;
        return max(maxLen, len(s) - resStart);

        """
        #fails for TestCase7
        if not s:
            return 0
        if len(s) == 1:
            return 1
        mylist = []
        maxlen = -sys.maxsize -1
        for i in range(len(s)):
            if s[i] in mylist:
                len_myList = len(mylist)
                if len_myList > maxlen:
                    maxlen = len_myList
                del mylist[:]
                mylist.append(s[i])
            else:
                mylist.append(s[i])
        len_myList = len(mylist)
        if len_myList > maxlen:
            return len_myList
        else:
            return maxlen
        """

s = Solution()
s.lengthOfLongestSubstring("pwwkew")
"""
Test Case #1
s.lengthOfLongestSubstring("abcabcbb")

Test Case #2
s.lengthOfLongestSubstring("bbbbb")

Test Case #3
s.lengthOfLongestSubstring("pwwkew")

Test Case #4
s.lengthOfLongestSubstring("")

Test Case #5
s.lengthOfLongestSubstring(" ")

Test Case #6
s.lengthOfLongestSubstring("au")

Test Case #7
s.lengthOfLongestSubstring("dvdf")
"""