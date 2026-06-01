#for circular doubly linklist 
#two conditions should changed ->
#1. (last.next = self.head    &
#   self.head.prev = last)
#2. while(t.next != self.head):
# last node contains the loc of head node.

class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # last node create/insert
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.head.next = self.head  # Point to self for circularity
            self.head.prev = self.head  # Point to self for circularity
            return

        # Find the last node
        last = self.head.prev
        last.next = temp
        temp.prev = last
        temp.next = self.head
        self.head.prev = temp

    # start node create/insert
    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.head.next = self.head
            self.head.prev = self.head
            return

        last = self.head.prev
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        self.head.prev = last
        last.next = self.head

    # insertion at mid / searching
    def insertAtMid(self, value, x):
        if self.head is None:
            print("Linked List is empty")
            return

        t = self.head
        while t.next != self.head:  # Condition changed
            if t.data == x:
                break
            t = t.next

        # Node to insert
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def printDLL(self):
        if self.head is None:
            print("Linked List is empty")
            return

        t1 = self.head
        # Traverse and print until we loop back to the head
        while True:
            print(t1.data, end=" <--> ")
            t1 = t1.next
            if t1 == self.head:
                break
        print("(Head)")

    # delete
    def deletionDLL(self, value):
        if self.head is None:
            print("Linked List is empty")
            return

        t = self.head

        # Case 1: Deletion from beginning
        if t.data == value:
            if t.next == self.head:  # Only 1 node
                self.head = None
                return
            last = self.head.prev
            self.head = t.next
            self.head.prev = last
            last.next = self.head
            return

        # Case 2: Deletion from middle or last
        t = self.head.next
        while t != self.head:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next

        print(f"Value {value} not found in the list.")


# Testing the structure
obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)

print("Circular Doubly Linked List:")
obj.printDLL()

print("\nInserting 25 after 20:")
obj.insertAtMid(25, 20)
obj.printDLL()

print("\nDeleting 30:")
obj.deletionDLL(30)
obj.printDLL()

obj.insertAtBeg(1)
obj.printDLL()
