"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # simple solution
        j = len(digits) - 1
        carry = 1
        while j >= 0:
            sum = digits[j] + carry
            if sum > 9:
                digits[j] = sum % 10
                carry = 1
            else:
                digits[j] = sum
                carry = 0
            j -= 1
        if carry:
            digits = [carry] + digits
        return digits

s = Solution()
print(s.plusOne([9,9]))

"""
TestCase #1
print(s.plusOne([1,2,3]))

TestCase #1
print(s.plusOne([9]))

TestCase #3
print(s.plusOne([9, 9]))
"""