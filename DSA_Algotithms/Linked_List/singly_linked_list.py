"""
+------+------+
|  10  |  *---|----+
+------+------+
                    |
                    v
                +------+------+
                |  20  |  *---|----+
                +------+------+
                                    |
                                    v
                                +------+------+
                                |  30  |  *---|----+
                                +------+------+
                                                    |
                                                    v
                                                +------+------+
                                                |  40  | None |
                                                +------+------+
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating node
# node_1 = Node(10)
# node_2 = Node(20)

"""
+------+------+
| data | next |
+------+------+
|  10  | None |
+------+------+
"""


# print(node_1.data)
# print(node_1.next)
# print(node_2.data)
# print(node_2.next)


# connecting node
# node_1.next = node_2
"""
node1
  |
  v
+------+------+
|  10  |  *---|------+
+------+------+      |
                     v
                +------+------+
                |  20  | None |
                +------+------+
"""
# print(node_1.data)
# print(node_1.next.data)
# print(node_2.data)
# print(node_2.next)



# Create Linked List

class LinkedList:
    def __init__(self):
        self.head = None

    # insert node
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:

            print(current.data, end= " -> ")
            current = current.next

        print("None")

    def search(self, value):

        current = self.head

        while current.next is not None:
            if current.data == value:
                return True

            current = current.next
        return False

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()

    def insert_at_the_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.display()

    def delete_node(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next


        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next

            current = current.next

        self.display()

    def find_nth_node(self, node_number):
        if node_number == 1:
            return self.head.data

        current = self.head
        num = 1
        while current is not None:
            if num == node_number:
                return current.data
            current = current.next
            num += 1
        return False

    def find_middle_node(self):
        current = self.head
        num = 1
        while current.next is not None:
            current = current.next
            num += 1
        print(f"total number of nodes: {num}")
        if num % 2 ==0:
            mid = num//2
        else:
            mid = (num//2) + 1
        current = self.head
        for i in range(mid-1):
            current = current.next
        print(f"middle node: {current.data}")



linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

linked_list.display()

print(linked_list.search(20))

linked_list.insert_at_beginning(50)

linked_list.insert_at_the_end(60)

linked_list.delete_node(50)

data = linked_list.find_nth_node(3)

print(data)

linked_list.find_middle_node()





