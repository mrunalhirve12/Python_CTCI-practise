"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import defaultdict, Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #O(N) and O(N) extra space

        # if both strings not present, return true; if one of them not present return False
        if not s and not t:
            return True
        elif not s or not t:
            return False

        # if length of two string not same return False
        if len(s) != len(t):
            return False

        # take counter and enumerate over string and check each char count
        x = Counter(s)
        y = Counter(t)
        for i, c in enumerate(s):
            if x[c] != y[c]:
                return False
        return True


        """
        # if both strings not present, return true; if one of them not present return False
        #NlogN solution 
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        # if length of two string not same return False
        if len(s) != len(t):
            return False
        
        #sort string 
        s = sorted(s)
        t = sorted(t)

        #check sorted string by iterating over it
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        """


s = Solution()
print(s.isAnagram("anagram", "nagaram"))

"""
Test Case #1
s.isAnagram("anagram", "nagaram")

Test Case #2
s.isAnagram("rat", "cat")

Test Case #3
s.isAnagram("", "")

Test Case #4
s.isAnagram("", "cat")
"""