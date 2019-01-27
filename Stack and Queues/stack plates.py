class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            raise NameError("Can't have stacks of that height")
        else:
            self.capacity = capacity

    def push(self, item):
        if not self.stacks:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if not self.stacks:
            raise NameError("can't pop an empty stack")
        else:
            popped_data = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popped_data

    def popAt(self, index):
        if not self.stacks:
            raise NameError("can't pop an empty stack")
        elif index - 1 > len(self.stacks):
            raise NameError("index is out of range")
        else:
            popped_data = self.stacks[index - 1][-1]
            if len(self.stacks[index - 1]) == 1:
                del self.stacks[-1]
            elif len(self.stacks) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index - 1][-1] = self.stacks[index][0]

                for i in range(index, len(self.stacks)):
                    for j in range(0, len(self.stacks[i]) - 1):
                        self.stacks[i][j] = self.stacks[i][j + 1]
                    if i < len(self.stacks) - 1:
                        self.stacks[i][-1] = self.stacks[i + 1][0]
                del self.stacks[-1][-1]
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
        return popped_data


print("Test 1b: make a stack with limit 4.")
print("push [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14]")
x = SetOfStacks(4)
for i in range(1, 15):
    x.push(i)
print(x.stacks == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14]])

print("Test 2b: pop 12 from stack 3")
print(x.popAt(3) == 12 and x.stacks == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 13], [14]])

print("Test 3b: pop 8 from stack 2")
print(x.popAt(2) == 8 and x.stacks == [[1, 2, 3, 4], [5, 6, 7, 9], [10, 11, 13, 14]])

print("Test 4b: pop 4 from stack 1")
print(x.popAt(1) == 4 and x.stacks == [[1, 2, 3, 5], [6, 7, 9, 10], [11, 13, 14]])
