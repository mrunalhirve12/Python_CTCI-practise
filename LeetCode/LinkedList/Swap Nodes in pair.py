#24. Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        elif not head.next:
            return head
        elif not head.next.next:
            tmp = head.next
            head.next.next = head
            head.next = None
            return tmp
        curr = head
        nxt = curr.next
        rec = nxt
        prev = ListNode(0)
        prev.next = curr
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr.next = tmp
            prev.next = nxt
            if not tmp:
                return rec
            prev = curr
            curr = tmp
            nxt = curr.next
        return rec


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

s = Solution()
s.swapPairs(l1)