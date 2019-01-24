class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        if self.head is None:
            self.head = Node(data)
            self.node = self.head
        else:
            # node = Node(data)
            self.node.next = Node(data)
            self.node = self.node.next

    def printl(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # ------------------O(n)------------------------
    def kthelement(self, k):
        self.node = self.head
        lenl = 0
        while self.node:
            lenl += 1
            self.node = self.node.next

        if k > lenl:
            print("k greater than length")

        self.node = self.head
        for i in range(0, lenl - k - 1):
            self.node = self.node.next
        print(self.node.data)

    # ---------If len of LL not known using pointers O(n)----------------------------
    def kthelementpointers(self, k):
        self.node = self.head
        self.ptr = self.head
        cnt = 0
        while cnt < k:
            self.ptr = self.ptr.next
            cnt += 1

        while self.ptr.next is not None:
            self.ptr = self.ptr.next
            self.node = self.node.next

        print(self.node.data)


l = LinkedList()
# l.insert_end(15)
# l.insert_end(14)
# l.insert_end(16)
# l.insert_end(15)
# l.insert_end(15)
# l.insert_end(14)

l.insert_start(18)
l.insert_start(159)
l.insert_start(15)
l.insert_start(10)
l.insert_start(15)
l.insert_start(14)

l.printl()
print("===============")

l.kthelement(2)

l.kthelementpointers(2)
