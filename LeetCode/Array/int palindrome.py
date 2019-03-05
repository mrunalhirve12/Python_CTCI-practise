"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if x is negative, number will not be a palindrome
        if x < 0:
            return False
        #checks if both numbers are same, then return True, else return False
        if x == self.reverse(x):
            return True
        return False

    def reverse(self,x):
        #res store the result
        res = 0
        #till x is greater than 0; reverse the number
        while x > 0:
            #example x= 123, 123% 10 gives 3
            #res initilally 0, res = 3;
            res = res * 10 + x % 10
            # x will be less than 1 digit, 123/10 gives 12
            x = int(x /10)
        #returns the number
        return res
"""
s= Solution
#Test Case 1
s.isPalindrome(s,121)

#Test Case 2
s.isPalindrome(s,-121)

#Test Case 2
s.isPalindrome(s,134)
"""