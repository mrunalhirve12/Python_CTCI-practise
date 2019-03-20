"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #base case no digit
        if not len(digits):
            return []

        combination = {"1": "","2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8":"tuv","9":"wxyz"}
        #list is empty
        lists = []
        lists.append("")

        #if digit contains other than digit
        if not digits.isdigit():
            return lists

        #iterate through each digit
        for i in digits:
            if i == "1":
                continue

            #forming combination of each letters
            if i in combination:
                letters = combination[i]
                tmp = []
                for letter in letters:
                    for element in lists:
                        tmp.append(element+letter)
                lists = tmp
        return lists



s = Solution()
s.letterCombinations("  42")
"""
Test Case #1
s.letterCombinations("23")

Test Case #2
s.letterCombinations("-30")

Test Case #3
s.letterCombinations("4193 with words")

Test Case #4
s.letterCombinations("words and 987")

Test Case #5
s.letterCombinations("-91283472332")

Test Case #6
s.letterCombinations("  -42")

Test Case #7
s.letterCombinations(" ")
"""