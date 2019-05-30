class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


def inserthead(head, k):
    newnode = ListNode(k)
    newnode.next = head
    head = newnode
    return head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

inserthead(l1, 0)
