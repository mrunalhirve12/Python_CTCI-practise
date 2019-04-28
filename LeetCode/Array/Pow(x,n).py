"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def myPow(self, x, n):
        """
        #:type x: float
        #:type n: int
        #:rtype: float

        # The trick is to evaluate a**n as (a**(n/2))**2 when n is even, and as a*(a**((n-1)/2))**2 when n is odd.
        # Recursive algorithm: Time complexity O(log n), space complexity O(log n) (implicit stack for recursion)
        def recursion(x, n):
            # if power is 0; then return 1
            if n == 0:
                return 1
            # else recursively do n/2
            # if even power multiply res by res
            # else multiply x * res * res
            else:
                res = recursion(x, int(n / 2))
                if n % 2 == 1:
                    return res * res * x
                else:
                    return res * res
        # if power is negative than do 1/recursion
        recip = False
        if n < 0:
            recip = True
            n = -n
        if recip:
            return 1 / recursion(x, n)
        else:
            return recursion(x, n)
        """

        # Iterative solution
        if n == 0:
            return 1
        elif x == 0:
            return 1
        recip = False
        if n < 0:
            recip = True
            n = -n

        res = 1
        y = x
        while n > 0:
            if n % 2 ==1:
                res *= x
                n -= 1
            else:
                x = x * x
                n /= 2

        if recip:
            return 1/ res
        else:
            return res

s = Solution()
s.myPow(2.00000, 10)
