"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import itertools
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = defaultdict(list)
        for i in strs:
            #appends multiple strings to sorted keys
            dict["".join(sorted(i))].append(i)
        #return list of values
        return list(dict.values())


        """
        #Dont know how groupby works
        dict = defaultdict(list)
        for i in strs:
            x = "".join(sorted(i))
            dict[i] = x

        groups = itertools.groupby(dict, key=dict.values())
        print(groups)
        """



s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])