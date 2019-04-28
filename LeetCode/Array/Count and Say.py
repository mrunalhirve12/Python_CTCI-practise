"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # if no is 1 return '1'
        if n == 1:
            return '1'
        # if not 1; initialize x to 1
        # keep decrement n and pass to function x
        x = '1'
        while n > 1:
            x = self.count(x)
            n -= 1
        return x

    def count(self, x):
        # list of x
        m = list(x)
        # ans list
        ans = []
        # Append None to m
        m.append(None)
        i, j = 0, 0
        # keep iterating loop till len m
        while i < len(m) - 1:
            j += 1
            if m[j] != m[i]:
                ans += [j - i, m[i]]
                i = j
        return ''.join(str(s) for s in ans)


s = Solution()
print(s.countAndSay(4))
