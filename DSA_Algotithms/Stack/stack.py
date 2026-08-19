class Stack:

    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def push(self, value):

        if len(self.items) == self.capacity:
            raise OverflowError("Stack Overflow")

        self.items.append(value)

    def pop(self):

        if not self.items:
            raise IndexError("Stack Underflow")

        return self.items.pop()

    def peek(self):

        if not self.items:
            raise IndexError("Stack is empty")

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def size(self):
        return len(self.items)


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
# stack.push(6) # ==> stack overflow

print(stack.peek())
print(stack.size())
print(stack.is_full())



