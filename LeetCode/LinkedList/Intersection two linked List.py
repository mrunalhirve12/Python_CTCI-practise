"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def move(self, root, diff):
        tmp = root
        for i in range(diff):
            tmp = tmp.next
        return tmp

    def count(self, root):
        cnt = 0
        while root:
            root = root.next
            cnt = cnt + 1
        return cnt

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #if not headA and not headB return None
        if not headA or not headB:
            return None

        #count no. of Nodes
        m1 = self.count(headA)
        m2 = self.count(headB)

        #calculate diff between two nodes
        diff = abs(m1 - m2)

        #sshift pointer till no diff
        if m1 > m2:
            headA = self.move(headA, diff)
        else:
            headB = self.move(headB, diff)

        #if nodes same, return it else continue
        while True:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next


l1 = ListNode(0)
l1.next = ListNode(9)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(4)

l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(4)


s = Solution()
s.getIntersectionNode(l1, l2)

