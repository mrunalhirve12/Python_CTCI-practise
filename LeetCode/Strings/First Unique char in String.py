"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # append char count  in default dict // We can also use counter instead
        dict = defaultdict(int)
        for i in s:
            dict[i] += 1
        # iterate through string if value is 1, return index(this will give me first occurrence), else return -1
        for i, c in enumerate(s):
            if dict[c] == 1:
                return i
        return -1

        """
        d=Counter(s)
        for i,c in enumerate(s):
            if d[c]==1:
                return i
        return -1
        """

s = Solution()
print(s.firstUniqChar("leetcode"))