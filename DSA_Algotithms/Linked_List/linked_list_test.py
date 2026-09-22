# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        if self.head == None:
            print("Empty Linked List")
            return

        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print()
        return

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                print(value)
                current.next = current.next.next
                return
            current = current.next
        print("not found")


# ll = LinkedList()
# ll.insert(5)
# ll.insert(6)
# ll.insert(7)
# ll.insert(8)
# ll.display()
# ll.insert_at_beginning(9)
# ll.display()
# ll.delete(9)
# ll.display()
# ll.delete(8)
# ll.display()
# ll.delete(6)
# ll.display()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return

    def forward_display(self):
        current = self.head
        while current is not None:
            print(current.data, end="<==>")
            current = current.next
        print()


    def reverse_display(self):
        current = self.tail
        while current is not None:
            print(current.data, end="<==>")
            current = current.prev
        print()

    def delete(self, value):
        current = self.head

        while current is not None:

            #delete head
            if current == self.head:
                self.head = current.next

                if self.head is not None:
                    self.head.prev = None

                else:
                    self.tail = None




dll = DoublyLinkedList()
dll.insert(4)
dll.forward_display()
dll.insert(5)
dll.forward_display()
dll.insert(6)
dll.forward_display()
dll.reverse_display()
dll.insert_at_beginning(7)
dll.forward_display()
dll.reverse_display()




