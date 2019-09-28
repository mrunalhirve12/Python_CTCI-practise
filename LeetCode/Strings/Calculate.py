"""def calculate(s):
    s = s.split()
    print(s)
    for i, c in enumerate(s):
        if c == '*':
            res = int(s[i-1]) * int(s[i+1])
            s[i - 1] = str(res)
            s.pop(i+1)
            s.pop(i)
    for i, c in enumerate(s):
        if c == '+':
            res = int(s[i-1]) + int(s[i+1])
            s[i - 1] = str(res)
            s.pop(i+1)
            s.pop(i)
    return res
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, [1]
        for i in s + "+":
            if i.isdigit():
                num = 10 * num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
        return res


s = Solution()
print(s.calculate("(5.0+2.0)*2.12"))
