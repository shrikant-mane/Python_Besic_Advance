"""
None ← 10 ⇄ 20 ⇄ 30 ⇄ 40 → None
        ↑                   ↑
       head                tail
"""
from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# node_1 = Node(10)
# node_2 = Node(20)
#
# node_1.next = node_2
# node_2.prev = node_1
#
# print(node_1.next.data)
# print(node_2.prev.data)

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

        # At a time only one change (next/prev) not both at once
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.forward_display()

    def search(self, value):
        if self.head == value:
            return True
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def forward_display(self):
        current = self.head
        while current is not None:
            print(current.data, end='<>')
            current = current.next
        print("None")

    def backword_display(self):
        current = self.tail
        while current is not None:
            print(current.data, end="<>")
            current = current.prev
        print("None")


    def delete(self, value):
        current = self.head

        while current is not None:

            if current.data == value:

                # delete head
                if current == self.head:
                    self.head = current.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None
                    self.forward_display()
                    return

                # Delete Tail
                if current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                    self.forward_display()
                    return

                # Delete Middle
                current.prev.next = current.next
                current.next.prev = current.prev
                self.forward_display()
                return

            current = current.next




doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(10)
doubly_linked_list.insert(20)
doubly_linked_list.insert(30)
doubly_linked_list.insert(40)

print("forward display")
doubly_linked_list.forward_display()
print()

print("backward display")
doubly_linked_list.backword_display()
print()

print("insert at beginning")
doubly_linked_list.insert_at_beginning(50)
print()

print(f"Search : {doubly_linked_list.search(30)}")

doubly_linked_list.delete(50)

doubly_linked_list.delete(30)

doubly_linked_list.delete(40)


