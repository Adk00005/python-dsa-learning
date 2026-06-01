#can be traverse forword or backword.
#contains 3 blocks on each node -> previous loc, data, next loc.
#we should have to make two pointers prev and next contains prev node loc and next node loc.
#last none contains None loc.

class Node:
    def __init__(self, value=None):
        self.data = value 
        self.next = None 
        self.prev = None 

#create DLL
class DoublyLL:
    def __init__(self):
        self.head = None 
    
    #last node create/insert
    def insertAtEnd(self, value):
        temp = Node(value) 
        if(self.head == None):
            self.head = temp 
            return 

        t = self.head 
        while (t.next != None):
            t = t.next  

        t.next = temp 
        temp.prev = t 

    #start node create/insert
    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp 
            return 
        temp.next = self.head 
        self.head.prev = temp 
        self.head = temp

    #insertion at mid 
    #searching code as well contains in insertion at mid
    def insertAtMid(self, value, x):
        t = self.head 

        while(t.next != None):   #searching loop
            if(t.data == x):
                break
            else:
                t = t.next     # upto this line for searching
        temp = Node(value)
        temp.next = t.next 
        t.next.prev = temp 
        t.next = temp 
        temp.prev = t 


    def printDLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <--> ")
            t1 = t1.next 
        print(t1.data)

    #delete
    def deletionDLL(self, value):
        if(self.head == None):
            print("Linked List is empty")
            return 
        
        t = self.head 
        #deletion from begining
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        
        #deletion from middle
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev 
                return
            else:
                t = t.next 

        #deletion from last 
        if(t.data == value):
            t.prev.next = None 


obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(50, 20)
obj.deletionDLL(5)
obj.deletionDLL(50)
obj.deletionDLL(40)
obj.printDLL()