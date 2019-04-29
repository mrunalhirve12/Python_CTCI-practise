"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        # NAIVE CODE
        strLen = len(s)
        tarLen = len(t)
        windowsize = tarLen
        while windowsize <= strLen :
            for i in range(strLen - windowsize+1):
                x = s[i:i+windowsize]
                dictT = collections.Counter(t)
                for i, c in enumerate(t):
                    if c not in x:
                        break
                    else:
                        dictT[c] -= 1
                if all(value == 0 for value in dictT.values()):
                    return x
            windowsize += 1
        return ""
    """
        #  a dictionary to record the index of each character of T
        #  Each time I found a window, (when miss == []),
        #  I checked the length of this window by subtracting the maximum index and the minimum index of the characters
        #  If this window is the smallest one so far, I record its beginning and ending index as "start" and "end."
        indices = {}
        for char in t:
            indices[char] = []
        miss = list(t)
        start = 0
        end = len(s)
        for i in range(len(s)):
            if s[i] in t:
                if s[i] not in miss and indices[s[i]] != []:
                    indices[s[i]].pop(0)
                elif s[i] in miss:
                    miss.remove(s[i])
                indices[s[i]].append(i)
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[0] for x in indices.values()])
                if maximum - minimum + 1 < end - start + 1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return s[start:end + 1]


s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))

"""
TestCase: #1
s.minWindow("ADOBECODEBANC","ABC")

TestCase: #2
s.minWindow("a","a")


TestCase: #3
s.minWindow("bbaa","aba")   //NAIVE code fails to handle duplicates
"""