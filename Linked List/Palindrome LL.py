class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.data = None
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

    def isPalindrome(self):
        """ Check if linked list is palindrome and return True/False."""
        node = self.head
        fast = node
        prev = None

        # prev approaches to middle of list till fast reaches end or None
        while fast and fast.next:
            fast = fast.next.next
            temp = node.next  # reverse elemets of first half of list
            node.next = prev
            prev = node
            node = temp

        if fast:  # in case of odd num elements
            tail = node.next
        else:  # in case of even num elements
            tail = node

        while prev:
            # compare reverse element and next half elements
            if prev.data == tail.data:
                tail = tail.next
                prev = prev.next
            else:
                return False

        return True



l = LinkedList()
l.insert_start(1)
l.insert_start(2)
l.insert_start(3)
l.insert_start(5)
l.insert_start(3)
l.insert_start(2)
l.insert_start(1)

l.printl()
print("===============")

if l.isPalindrome():
    print("Yes")
else:
    print("No")


#to see CTCI solution 1 and recursive
