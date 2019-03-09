"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # get the length of string having min lenght
        # min (iterable, key )
        minL = min(strs, key=len) if strs else ""
        # check for minL incase strs [] and minL is 0
        if len(minL) > 0:
            #iterate through len of minL
            for i in range(len(minL)):
                #check for previous chars in subsequent strs
                for j in range(len(strs)):
                    # if not equal, returns strs[0] before all chars match
                    if strs[j][i] != strs[0][i]:
                        return strs[0][:i]
        # else return strs[0] upto char (incase not match at all)
        return strs[0][:i + 1] if minL else ""


s = Solution
s.longestCommonPrefix(s,["a"])

"""
Test Case #1
s = Solution
s.longestCommonPrefix(s,["flower","flow","flight"])

Test Case #2
s = Solution
s.longestCommonPrefix(s,["dog","racecar","car"])

Test Case #3
s = Solution
s.longestCommonPrefix(s,[])

Test Case #4
s = Solution
s.longestCommonPrefix(s,["a"])

Test Case #4
s = Solution
s.longestCommonPrefix(s,["flow","flow","flow"])
"""