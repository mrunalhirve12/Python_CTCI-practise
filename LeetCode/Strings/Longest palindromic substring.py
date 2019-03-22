"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ''
        #initiliaze the table
        table = [[0 for x in range(n)] for y in range(n)]

        # All substrings of length 1 are palindromes
        # i.e making diagonal elements set to True
        maxlen = 1
        i = 0
        while i < n:
            table[i][i] = True
            ans = s[i]
            i = i + 1

        # check for sub-string of length 2.
        start = 0
        i = 0
        while i < n-1:
            if (s[i] == s[i+1]):
                table[i][i+1] = True
                start = i
                maxlen = 2
                ans = s[i: i+2]
            i = i + 1

        # Check for lengths greater than 2.
        # k is length of substring
        k =3
        while k <= n:
            i = 0
            # iterate through n - k + 1
            while i < n - k + 1:
                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1

                # checking for sub-string from
                # ith index to jth index iff
                # st[i+1] to st[(j-1)] is a
                # palindrome
                if table[i + 1][j -1] and s[i] == s[j]:
                    table[i][j] = True

                    if k > maxlen:
                        start = i
                        maxlen = k
                        ans = s[i:j+1]
                i = i + 1
            k = k + 1
        return  ans

s = Solution()
s.longestPalindrome("cbbd")

"""
Test Case #1
s.longestPalindrome("babad")

Test Case #2
s.longestPalindrome("cbbd")

Test Case #3
s.longestPalindrome("a")

Test Case #3
s.longestPalindrome("caba")
"""