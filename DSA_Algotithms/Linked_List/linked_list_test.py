class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):

        if self.head is None:
            print("empty linked_list")

        current = self.head

        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.display()

    def insert_at_the_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

        self.display()

    def search(self, value):
        if self.head.data == value:
            return True

        current  = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            self.display()

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self.display()
                return

            current = current.next



linked_list = LinkedList()
linked_list.display()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.display()

linked_list.insert_at_beginning(50)

linked_list.insert_at_the_end(40)

print(linked_list.search(10))
print(linked_list.search(30))
print(linked_list.search(40))
print(linked_list.search(100))

linked_list.delete(50)
linked_list.delete(30)
linked_list.delete(40)
