#for circular singly linklist 
#two conditions should changed ->
#1. (last.next = self.head 
#2. while(t.next != self.head):

class Node: 
    def __init__(self, info, next=None): 
        self.data = info 
        self.next = next 

class CircularLinkedList: 
    def __init__(self, head=None): 
        self.head = head 

    def insertAtEnd(self, value): 
        temp = Node(value) 
        if self.head != None: 
            t1 = self.head 
            # Rule 2: while(t.next != self.head)
            while t1.next != self.head: 
                t1 = t1.next 
            t1.next = temp 
            temp.next = self.head  # Make it circular
        else: 
            self.head = temp 
            temp.next = self.head  # Points to itself

    def insertAtBeg(self, value): 
        temp = Node(value) 
        if self.head != None: 
            t1 = self.head 
            # Find the last node to update its next pointer
            while t1.next != self.head: 
                t1 = t1.next 
            temp.next = self.head 
            t1.next = temp 
            self.head = temp 
        else: 
            self.head = temp 
            temp.next = self.head 

    def insertInMid(self, value, x): 
        temp = Node(value) 
        if self.head == None:
            return
        t1 = self.head 
        # Traverse the circular list safely
        while True:
            if t1.data == x: 
                temp.next = t1.next 
                t1.next = temp 
                break
            t1 = t1.next 
            if t1 == self.head: # Break if we made a full circle
                break

    def deleteLL(self, value): 
        if self.head == None: 
            return

        t1 = self.head 
        prev = None 

        # Case 1: Node to delete is the head
        if t1.data == value: 
            # If it's the only node in the list
            if t1.next == self.head: 
                self.head = None 
                return
            else: 
                # Find last node to update its circular reference
                last_node = self.head # Rule 1: last_node = self.head
                while last_node.next != self.head: 
                    last_node = last_node.next 
                self.head = t1.next 
                last_node.next = self.head 
                return

        # Case 2: Node to delete is in the middle or end
        prev = t1 
        t1 = t1.next 
        while t1 != self.head: 
            if t1.data == value: 
                prev.next = t1.next 
                return 
            prev = t1 
            t1 = t1.next 

    def printLL(self): 
        if self.head == None: 
            print("List is empty") 
            return 
        t1 = self.head 
        while True: 
            print(t1.data) 
            t1 = t1.next 
            if t1 == self.head: 
                break 

# Driver execution mirroring your original script
obj = CircularLinkedList() 
obj.insertAtEnd(10) 
obj.insertAtEnd(20) 
obj.insertAtEnd(30) 
obj.insertAtBeg(5) 
obj.insertInMid(40, 20) 
obj.deleteLL(30) 
obj.printLL()
