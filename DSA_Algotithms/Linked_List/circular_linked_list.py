

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None


    # Insert node at the beginning
    def insert_to_head(self, data):

        new_node = Node(data)

        # If linked list is empty
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return

        # If linked list is not empty
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head
        self.head = new_node


    # Display the linked list
    def display(self):

        if self.head is None:
            print("Circular Linked List Is Empty")

        current = self.head
        while True:
            print(f"{current.data}", end="->")
            current = current.next

            if current == self.head:
                break

        print("Break to the head")


    def insert_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head


    def search(self, value):
        if self.head is None:
            print(f"CLL is empty")

        current = self.head
        while True:
            if current.data == value:
                return True

            current = current.next

            if current == self.head:
                break
        return False


    def delete(self, value):
        if self.head is None:
            print("Empty cll")

        # In case only one node
        if self.head.next == self.head:
            if self.head.data == value:
                self.head = None
            return

        current = self.head
        previous = None

        while True:
            if current.data == value:

                # Deleting head
                if current == self.head:
                    last = self.head
                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                else:
                    previous.next = current.next

                print(f"{value} deleted")
                return

            previous = current
            current = current.next

            if current == self.head:
                break
        print(f"{value} not found")





cll = CircularLinkedList()
cll.insert_to_head(1)
cll.insert_to_head(2)
cll.insert_to_head(3)
cll.display()
cll.insert_to_end(5)
cll.insert_to_end(6)
cll.display()
print(cll.search(5))
print(cll.search(10))
cll.delete(11)
cll.display()

cll.delete(3)
cll.display()
cll.delete(1)
cll.display()
cll.delete(6)
cll.display()

