"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


Note:

You must return the copy of the given head as a reference to the cloned list.
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #if head is None
        if head is None:
            return None

        #add cloned node after each node
        temp = head
        while temp != None:
            next = temp.next
            temp.next = Node(temp.val, temp.next, Node)
            temp = next

        # 2nd step, setup random pointer
        temp = head
        while temp != None:
            if temp.random != None:
                temp.next.random = temp.random.next

        # 3rd step, split original and new list
        temp = head
        final = head.next
        temp2 = head.next
        while temp != None:
            temp.next = temp.next.next
            temp = temp.next

            if temp2.next != None:
                temp2.next = temp.next

            temp2 = temp2.next

        return final



l2 = Node(2, None, None)
l1 = Node(1, None, None)
l1.next = l2
l1.random = l2
l2.next = None
l2.random = l2


s = Solution()
s.copyRandomList(l1)