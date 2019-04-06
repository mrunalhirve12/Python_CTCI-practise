"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
from collections import Counter


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        # naive approach can be iterating over J and checking in S; and counting vals and chk
        
        # if not J or not S
        if not J or not S:
            return 0
        
        # initialize count
        count = 0
        # initialize counter maintaining count of each var
        y = Counter(S)
        # iterate through loop y counter, if char of y present in jewels count
        for i, c in enumerate(y):
            if c in J:
                count += y[c]
        return count
        """

        # Approach 3: direct count without dict
        # initialize count
        cnt = 0
        # if char in Jewels
        for l in J:
            # increment count by getting count of chars in stone
            cnt = cnt + S.count(l)
        return cnt



s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))

"""
Test Case #1
s.isAnagram("aA", "aAAbbbb")

Test Case #2
s.isAnagram("z", "ZZ")
"""