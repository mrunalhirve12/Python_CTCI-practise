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
    def delete_first(self):
        self.node = self.head
        if self.node is None or self.node.next is None:
            return False
        else:
            next = self.node.next
            self.node.data = next.data
            self.node.next = next.next
            return True

    def delete_middle(self):
        current = self.head
        self.node = self.head
        if current is None or current.next is None:
            return False
        while current.next:
            if current.next.next:
                self.node.next = current.next.next
                return True
        current = current.next

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

#l.delete_first()
#l.printl()

print("===============")
l.delete_middle()
l.printl()
