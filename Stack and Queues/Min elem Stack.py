#https://codereview.stackexchange.com/questions/43344/retrieve-min-from-stack-in-o1
class SmartStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def stack_push(self, x):
        self.stack.append(x)
        if not self.min or x <= self.stack_min():
            self.min.append(x)

    def stack_pop(self):
        x = self.stack.pop()
        if x == self.stack_min():
            self.min.pop()
        return x #return pops out from list

    def stack_min(self):
        return self.min[-1]

stack = SmartStack()
stack.stack_push(1)
stack.stack_push(1)
stack.stack_push(3)
stack.stack_pop()
stack.stack_pop()
print(stack.stack_min())