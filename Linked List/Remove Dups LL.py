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

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            # node = Node(data)
            self.node = Node(data)
            self.node.next = self.head
            self.head = self.node

    def printl(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # -------O(n2)--------------------------
    def removeDups(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def removeDupExt(self):
        s = set()
        self.node = self.head
        while self.node:
            if self.node.data in s:
                self.current.next = self.node.next
            else:
                s.add(self.node.data)
                self.current = self.node
            self.node = self.current.next


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

l.removeDupExt()
l.printl()
