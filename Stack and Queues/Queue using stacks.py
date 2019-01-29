class Stack:

    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0


class CreatingQueueWithTwoStacks:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if not self.stack_1.is_empty():
            while self.stack_1.size() > 0:
                self.stack_2.push(self.stack_1.pop())
            res = self.stack_2.pop()
            while self.stack_2.size() > 0:
                self.stack_1.push(self.stack_2.pop())
            return res

if __name__ == '__main__':
    q = CreatingQueueWithTwoStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    a = q.dequeue()
    print(a)
    b = q.dequeue()
    print(b)
    c = q.dequeue()
    print(c)
    d = q.dequeue()
    print(d)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())