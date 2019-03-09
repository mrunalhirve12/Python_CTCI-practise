class Solution:
    def reverse(self, x: int) -> int:
        # res store the result
        res = 0
        flag = False
        if x < 0:
            flag = True
            x = -1 * x
        # till x is greater than 0; reverse the number
        while x > 0:
            # example x= 123, 123% 10 gives 3
            # res initilally 0, res = 3;
            res = res * 10 + x % 10
            # x will be less than 1 digit, 123/10 gives 12
            x = x//10
        # returns the number
        if res > pow(2, 31) - 1 or res < -pow(2, 31):
            return 0
        elif flag == True:
            res = -1 * res
            return res
        else:
            return res

"""
s= Solution
#Test Case 1
s.reverse(s,121)

#Test Case 2
s.reverse(s,-121)

#Test Case 3
s.reverse(s,120)

#Test Case 4
s.reverse(s,15678934509)
"""


