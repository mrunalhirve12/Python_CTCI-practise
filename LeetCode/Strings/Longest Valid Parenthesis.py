"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(0, len(s)):
            if not stack:
                stack.append(i)
            else:
                if s[i] == ")" and s[stack[-1]] == "(":
                    stack.pop()
                    continue
                stack.append(i)
        end = len(s)
        if not stack: return end
        res = 0
        while stack:
            start = stack.pop()
            res = max(res, end - start - 1)
            end = start
        res = max(res, end)
        return res

s = Solution()
s.longestValidParentheses(")()())")