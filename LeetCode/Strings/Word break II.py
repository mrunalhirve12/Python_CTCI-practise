class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def dfs(i):
            if i == len(s):
                return [""]
            if i in dic:
                return dic[i]
            res = []
            for j in range(i, len(s)):
                head = s[i:j + 1]
                if head in wordSet:
                    tmp = dfs(j + 1)
                    for string in tmp:
                        string = head + " " + string
                        res.append(string.strip())
            dic[i] = res
            return res

        dic = {}
        wordSet = set(wordDict)
        return dfs(0)

s = Solution()
s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])