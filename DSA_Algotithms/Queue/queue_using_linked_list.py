class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return value

    def peek(self):

        if self.front is None:
            raise IndexError("Queue is empty")

        return self.front.data

    def is_empty(self):

        return self.front is None

    def size(self):

        count = 0
        current = self.front

        while current:
            count += 1
            current = current.next

        return count


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.size())
print(queue.peek())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
# print(queue.dequeue())  # ==> IndexError as queue is empty
