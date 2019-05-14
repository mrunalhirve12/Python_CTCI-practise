"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.


Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""
import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        """"
        # Fails for case #2
        paragraph = paragraph.lower()
        banned = set(banned)

        lis = paragraph.split(' ')
        dic = {}
        for word in lis:
            word = word.strip("?!',;.")
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] +=1

        maximum = 0
        char = ""
        for key, val in dic.items():
            if val > maximum:
                maximum = val
                char = key
        return char
    """
        paragraph = paragraph.lower()
        banned = set(banned)
        paragraph = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', ' ', paragraph)
        lis = paragraph.split()
        dic = {}
        for word in lis:
            #word = word.strip("?!',;.")
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1

        maximum = 0
        char = ""
        for key, val in dic.items():
            if val > maximum:
                maximum = val
                char = key
        return char

s = Solution()
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))

"""
TESTCASE #1
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

TESTCASE #2
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
"""