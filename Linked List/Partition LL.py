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

    def partitionpointers(self, x):
        current = runner = self.head
        while runner:
            if runner.data < x:
                temp = current.data
                current.data = runner.data
                runner.data = temp

                current = current.next
                runner = runner.next
            else:
                runner = runner.next



    def partitionmerge(self, x):
        self.node = self.head
        beforeStart = None
        beforeEnd = None
        afterStart = None
        afterEnd = None

        while self.node is not None:
            next = self.node.next
            self.node.next = None
            if self.node.data < x:
                if beforeStart is None:
                    beforeStart = self.node
                    beforeEnd = beforeStart
                else:
                    beforeEnd.next = self.node
                    beforeEnd = self.node
            else :
                if afterStart is None:
                    afterStart = self.node
                    afterEnd = afterStart
                else:
                    afterEnd.next = self.node
                    afterEnd = self.node
            self.node = next

        if beforeStart is None:
            return afterStart

        beforeEnd.next = afterStart
        return beforeStart


l = LinkedList()
# l.insert_end(15)
# l.insert_end(14)
# l.insert_end(16)
# l.insert_end(15)
# l.insert_end(15)
# l.insert_end(14)

l.insert_start(3)
l.insert_start(5)
l.insert_start(8)
l.insert_start(5)
l.insert_start(10)
l.insert_start(2)
l.insert_start(1)

l.printl()
print("===============")

l.partitionmerge(5)
l.printl()


print("===============")
l.partitionpointers(5)
l.printl()
