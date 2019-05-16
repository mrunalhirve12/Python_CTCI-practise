"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # TIME  AND SPACE COMPLEXITY O(N)
        # update the last index value in dict
        """
        dic = {}
        for i, char in enumerate(S):
            dic[char] = i
        # will need a res list to maintain string lists, currLen and highest index stored
        res = []
        currLen = 0
        hi = 0
        # iterate through the loop, store the highest index(so that each letter appears in at most one part)
        for i, char in enumerate(S):
            # if the index of chars same as index
            if dic[char] == i:
                # check if the index as same as hi (that will be a string), calculate its length and update current
                if hi == i:
                    res.append(i - currLen + 1)
                    currLen = i + 1
                # if char having index greater than hi, length will be 1 an
                elif hi < i:
                    res.append(1)
                    currLen = i + 1
            # store the highest index of chars
            elif dic[char] > hi:
                hi = dic[char]
        return res
        """
        dict = {}
        for i, ch in enumerate(S):
            dict[ch] = i
        hi = 0
        count = 1
        res = []
        for i in range(len(S) - 1):
            if hi < dict[S[i]]:
                hi = dict[S[i]]
            if hi == i:
                l = count
                res.append(l)
                count = 0
            count += 1
        res.append(count)
        return res


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))

"""
Test Case #1
print(s.partitionLabels("ababcbacadefegdehijhklij"))

Test Case #2
print(s.partitionLabels("eaaaabaaec"))
"""