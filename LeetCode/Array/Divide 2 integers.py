"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""
class Solution(object):
    MAX_INT = 0x7FFFFFFF

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        # Naive
        count = 0
        neg = False
        if divisor < 0:
            divisor = -1 * divisor
            neg = True
        elif dividend < 0:
            dividend = -1 * dividend
            neg = True
        while dividend > divisor:
            dividend = dividend - divisor
            count += 1
        return count * -1 if neg else count
        """

        # for faster division; add value by doubling it
        #if divisor == 0:
        #    return self.MAX_INT
        if dividend == 0:
            return 0
        negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            x = divisor
            i = 1
            while dividend >= x + x:
                x += x
                i += i
            dividend -= x
            ans += i
        ans =  self.MAX_INT if not negative and ans > self.MAX_INT else ans
        return -ans if negative else ans

s = Solution()
print(s.divide(10,3))
"""
TESTCASE #1
print(s.divide(10,3))

TESTCASE #2
print(s.divide(1,1))

TESTCASE #3
print(s.divide(-2147483648, -1))
"""