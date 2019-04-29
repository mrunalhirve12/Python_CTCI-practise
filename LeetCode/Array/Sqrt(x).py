"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # idea is the get range or mid til mid * mid should not be greater than no; return lowest since we want to truncate the decimals
        # set low and high
        low = 0
        high = x
        mid = (low + high)/2
        if mid == 0:
            return high
        while high - low != 1:
            mid = (high + low) //2
            if mid * mid > x:
                high = mid
            else:
                low = mid
        return low

s = Solution()
s.mySqrt(10)