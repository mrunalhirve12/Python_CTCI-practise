from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:  # backtracking
            res.append(path)
        for i in xrange(1, len(s) + 1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPar(self, s):
        return s == s[::-1]

s = Solution()
s.partition("aab")