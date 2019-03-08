"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # if len is 0, it is valid
        if len(s) == 0:
            return True
        # if len is 1, then it is invalid parenthesis
        elif len(s) == 1:
            return False
        stack = []
        dict = {'}': '{', ']':'[', ')':'('}
        brackets = [')','}',']']
        #iterating through s
        for i in range(len(s)):
            #if first element belongs to bracket, it is invalid parenthesis
            if s[0] in brackets:
                return False
            if s[i] not in brackets:
                stack.append(s[i])
            else:
                #check len of stack and top element before popping
                if len(stack)!= 0 and s[i] in dict and dict[s[i]] == stack[-1]:
                    stack.pop()
                #if len of stack is 0 and element present e.g "[])", then return False
                else:
                    return False
        return not stack

s = Solution
"""
#TestCase 1:
Input: "()"

#TestCase 2:
Input: "()[]{}"

#TestCase 3:
Input: "(]"

#TestCase 4:
Input: "([)]"

#TestCases 5:
Input: "{[]}"

#TestCases 6:
Input: "]"

#TestCases 6:
Input: "){"

#TestCases 7:
Input: "[])"

#TestCases 7:
Input: ""
"""
if s.isValid(s,""):
    print("True")
else:
    print("False")
