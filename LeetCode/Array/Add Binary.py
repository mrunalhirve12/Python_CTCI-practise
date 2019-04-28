"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # logic: reverse and then add each (similar to add two list)
        a = a[::-1]
        b = b[::-1]
        i = 0
        j = 0
        res = []
        carry = 0
        while i < len(a) or j < len(b):
            sum = (int(a[i]) if i < len(a) else 0) + (int(b[j]) if j < len(b) else 0) + carry
            if sum == 1:
                res.append(1)
                carry = 0
            elif sum == 2:
                res.append(0)
                carry = 1
            elif sum == 3:
                res.append(1)
                carry = 1
            else:
                res.append(0)
                carry = 0
            i += 1
            j += 1
        if carry:
            res.append(carry)
        res = res[::-1]
        return "".join(str(v) for v in res)

s = Solution()
print(s.addBinary("1010", "1011"))