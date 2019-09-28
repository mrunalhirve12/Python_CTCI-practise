"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq
from heapq import heappush, heappop

# Definition for singly-linked list.
from pip._vendor.msgpack.fallback import xrange


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        ??????? Not clear
        
        ans = []
        heap = []
        for i in xrange(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            top = heapq.heappop(heap)
            ans.append(top[0])
            if top[1].next:
                heapq.heappush(heap, (top[1].next.val, top[1].next))
        return ans

        """
        dummy = ListNode(0)
        heap = [(x.val,x) for x in lists if x]
        heapq.heapify(heap)
        cursor = dummy
        while heap:
            _,node = heapq.heappop(heap)
            cursor.next = node
            cursor = cursor.next
            if node.next:
                heapq.heappush(heap,(node.next.val,node.next))
        return dummy.next


        """
        If linked list given
        if not lists:
            return []
        all = []
        for node in lists:
            while node:
                all.append(node.val)
                node = node.next
        all.sort()

        if not all: return []
        result = inloop = ListNode(all[0])
        for n in range(1, len(all)):
            inloop.next = ListNode(all[n])
            inloop = inloop.next
        return result
        """


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

s = Solution()
s.mergeKLists([l1,l2,l3])

"""
Test Cases #1
s = Solution
l1 = mergeKLists([l1,l2,l3])


s = Solution
s = mergeKLists([])
"""
