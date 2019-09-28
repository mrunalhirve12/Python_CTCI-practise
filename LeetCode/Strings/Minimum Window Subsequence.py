from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        n = len(S)
        m = len(T)

        dic = dict()
        for i, s in enumerate(T):
            dic.setdefault(s, []).append(i)

        dp = [-1 for i in xrange(m)]

        count = n + 1
        start = -1

        for index, c in enumerate(S):
            if c in dic:
                for i in dic[c][::-1]:
                    if i == 0:
                        dp[i] = index
                    else:
                        dp[i] = dp[i - 1]
                    if i == m - 1 and dp[i] >= 0 and index - dp[i] + 1 < count:
                        count = index - dp[i] + 1
                        start = dp[i]
        if dp[-1] < 0:
            return ""
        return S[start:start + count]

s = Solution()
s.minWindow("abcdebdde", "bde")