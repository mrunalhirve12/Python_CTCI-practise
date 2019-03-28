"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2
"""
import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)

        """
        self.stack.append(x)
        if self.stack[-1] <= self.min_element:
            self.min_element = self.stack[-1]
            self.min_stack.append(self.min_element)
        """

    def pop(self):
        """
        :rtype: None
        """
        tmp = self.stack.pop()
        if tmp == self.min_stack[-1]:
            self.min_stack.pop()

        """
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        """

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack :
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
#["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
#[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
obj = MinStack()
obj.push()
obj.push()
obj.push()
obj.top()
obj.push(4)
obj.pop()
obj.push(4)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()