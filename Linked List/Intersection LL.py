class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printl(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def intersect(self, first, second):
        thisone = first
        otherone = second
        retval = LinkedList ()
        while thisone and otherone:
            if otherone.data > thisone.data:
                thisone = thisone.next
            elif thisone.data > otherone.data:
                otherone = otherone.next
            else:
                reval.push(otherone.data)
                thisone = thisone.next
                otherone = otherone.next
        return reval


first = LinkedList()
second = LinkedList()

first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(8)
print("First List is ")
first.printl()

second.push(4)
second.push(8)
print("\n Second List is ")
second.printl()

print("\n Intersection is ")
reval = LinkedList()
reval.intersect(first.head, second.head)
reval.printl()


