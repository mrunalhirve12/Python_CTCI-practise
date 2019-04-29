# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # O(NM) time, O(NM) space
        n, m = len(s), len(p)
        match = [[False for j in xrange(m + 1)] for i in xrange(n + 1)]

        # Base cases - empty string matches w/ empty pattern
        match[0][0] = True

        # empty string to nonempty pattern
        for i in xrange(1, m + 1):
            if i > 1 and p[i - 1] == '*':
                match[0][i] = match[0][i - 2]

        # DP cases
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                # If the string char equals the pattern char or the pattern is a dot,
                # there is a match if everything before matches
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    match[i][j] = match[i - 1][j - 1]

                # Star can only match if there is something before the star to match
                elif j > 1 and p[j - 1] == '*':

                    # If the character before the star matches char in the string,
                    # the star can match 0 of the char before it, or at least 1.
                    # match[i][j-2] is for matching 0, cause we need to skip the last 2
                    # characters in the pattern. match[i - 1][j] is for matching 1, cause
                    # we need to skip 1 character in the string, but keep the entire pattern
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        match[i][j] = match[i][j - 2] or match[i - 1][j]

                    # If the character before the star does not match the char in the string,
                    # then the only way to get a match is if the star matches 0 characters
                    else:
                        match[i][j] = match[i][j - 2]

        return match[n][m]

