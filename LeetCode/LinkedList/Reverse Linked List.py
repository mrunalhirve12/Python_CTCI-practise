"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #let curr point to start of the the LL
        curr = head
        #initialize prev and next to None
        prev = None
        next = None
        # while curr is not None(i.e end)
        while curr is not None:
            #store next first,
            # store prev in curr.next,
            # update prev and next
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

s = Solution()
print(s.reverseList(l1))

