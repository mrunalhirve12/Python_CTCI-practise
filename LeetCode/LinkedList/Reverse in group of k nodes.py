#25. Reverse Nodes in k-Group
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        #:type head: ListNode
        #:type k: int
        #:rtype: ListNode

        # Misses the first and last vals
        dummy = ListNode(-1)
        dummy.next = curr = head
        tail = None
        while curr.next:
            group = 0
            prev = None
            next = None
            while group < k and curr.next:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                group += 1
            if tail:
                tail.next = prev
            pp = prev
            while pp.next:
                pp = prev.next
            tail = pp
            #prev.next = next
            curr = next
        return dummy.next



        # Iterative : too complex to understand
        while not head or not head.next:
            return head
        if k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        record = dummy
        left = head
        nxt = head.next
        count = 1
        while True:
            while nxt and count < k:  # reverse links within a group
                tmp = nxt.next
                nxt.next = left
                prev = left
                left = nxt
                nxt = tmp
                count += 1
            if count == k:  # rotate the group
                tmp = dummy.next
                dummy.next = left
                tmp.next = nxt
                dummy = tmp
                count = 1
                left = nxt
                if nxt:
                    nxt = nxt.next
            else:
                if count >= 2:
                    left.next = None
                    if count > 2:  # the last group has size < k, and we need to reverse the links within the group again.
                        while True:
                            tmp = prev.next
                            prev.next = left
                            if tmp.next == prev:
                                return record.next
                            left = prev
                            prev = tmp
                return record.next
"""
        dummy = ListNode(-1)
        dummy.next, tail = head, dummy
        p = q = head
        i = 0
        while p:
            p = p.next
            i += 1
            if i == k:
                prev = p
                while q.next != p:
                    q.next, q, prev = prev, q.next, q
                tail.next, tail, q.next, q, i = q, tail.next, prev, p, 0
        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

s = Solution()
s.reverseKGroup(l1, 3)