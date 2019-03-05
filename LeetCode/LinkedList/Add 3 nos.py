"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #initialize carry to 0
        carry = 0
        # create a new List
        head = ListNode(0)
        res = head
        #check if either of the list are none, else return the other
        if not l1:
            res = l2
        elif not l2:
            res = l1
        #Addition function if l1 or l2 not none
        while l1 or l2:
            # getting addition of two nodes
            sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry
            #initilaize carry to 0 again
            carry = 0
            # if sum is greater than 10, set sum to mod and carry as 1
            if sum >= 10:
                sum = sum % 10
                carry = 1
            #storing result in new linkedList, and pointing to next node of the list
            res.next = ListNode(sum)
            res = res.next
            #iterate through next nodes of list
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        #check is last carry is 1
        if carry == 1:
            last = ListNode(1)
            res.next = last
        return head.next


"""
##########
Test Cases #1

s = Solution
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s.addTwoNumbers(s,l1,l2)

Test Cases #2
s = Solution
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = None
s.addTwoNumbers(s,l1,l2)


s = Solution
l1 = ListNode(1)
l1.next = ListNode(8)
l2 = None
s.addTwoNumbers(s,l1,l2)
"""


