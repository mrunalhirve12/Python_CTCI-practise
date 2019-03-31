"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #if not head
        if not head or not head.next:
            return True
        slow = head
        fast = head

        #calculate mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half of linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        #compare values
        while prev and head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(1)
l1.next.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(l1))


"""
#TESTCASE #1
[1,2,2,1]

#TESTCASE #1
[1,2,2,1,1]

#TESTCASE #1
[]
"""

        