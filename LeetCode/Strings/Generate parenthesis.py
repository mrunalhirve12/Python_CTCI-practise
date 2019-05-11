#https://leetcode.com/problems/generate-parentheses/discuss/215927/Python-solution

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # idea is to
        pairs = ["()"]
        i = 1
        while i < n:
            new_pairs = set()
            for p in pairs:
                for index, c in enumerate(p):
                    if c == "(":
                        new_pairs.add(p[0:index + 1] + "()" + p[index + 1:])
                new_pairs.add(p + "()")
            pairs = list(new_pairs)
            i += 1
        print(pairs)

s = Solution()
print(s.generateParenthesis(3))
