"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        #for remove duplicates
        wordList = self(wordList)
        #if endword not present return 0
        if endWord not in wordList:
            return 0
        #initialize count to 1
        ans = 1
        #create a list and append startword
        frontier = [beginWord]
        #make a set to keep track of visited words
        used = set(beginWord)
        #while words in frontier:
        while frontier:
            #initialize a new list
            nextLevel = []
            #iterate through word in frontier
            for word in frontier:
                #to chk only in the lenght of word
                for p in range(len(word)):
                    #iterating through all alpabet to find combinations
                    for c in string.ascii_lowercase:
                        #get combination of new word having len of word
                        newword = word[:p] + c + word[p + 1:]
                        #if word is endword then return
                        if word == endWord:
                            ans += 1
                            return ans
                        #if newword not in used and word is in worList, appeend in newlista and add in used
                        if newword not in used and newword in wordList:
                            used.add(newword)
                            nextLevel.append(newword)
            frontier = nextLevel
            ans += 1
        return 0



s = Solution()
s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])