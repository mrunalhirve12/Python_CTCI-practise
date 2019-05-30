#ToDo
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def util(head):
    first = head
    rest = head.next
    if rest == None:
        return
    recursiveReverse(rest)
    first.next.next = first

    first.next = None
    head = rest

def recursiveReverse(head):
    util(head)



l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

recursiveReverse(l1)