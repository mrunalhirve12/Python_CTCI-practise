"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str or len(str) < 1:
            return 0
        j = 0
        sign = '+'
        if str[j] == '-':
            sign = '-'
            j += 1
        elif str[j] == '+':
            j += 1

        result = 0
        while len(str) > j and str[j] >= '0' and str[j] <= '9':
            result = result * 10 + (ord(str[j]) - ord('0'))
            j += 1
        if sign == '-':
            result = -result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result


s = Solution()
"""
Test Case #1
s.myAtoi("42")

Test Case #2
s.myAtoi("-42")

Test Case #3
s.myAtoi("4193 with words")

Test Case #4
s.myAtoi("words and 987")

Test Case #5
s.myAtoi("-91283472332")

Test Case #6
s.myAtoi("  -42")

Test Case #7
s.myAtoi(" ")
"""

s.myAtoi("42")