class Queue:

    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        self.items.append(value)
        self.rear += 1

    def dequeue(self):
        if self.rear == self.front:
            return None
        value = self.items[self.front]
        self.front += 1
        return value

    def display(self):
        print(self.items[self.front:])

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.display()
print(queue.dequeue())
print(queue.dequeue())
queue.display()
print(queue.dequeue())
queue.display()
print(queue.dequeue())
print(queue.dequeue()) # ==> None