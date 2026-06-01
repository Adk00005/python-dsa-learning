#user defined data type - make a class.
#contains 2 blocks on each node i.e., info - data and its address.
#first node is called head and next to it called as head.next.
#properties - 
#1.non-contiguous
#2.heterogeneous
#3.need to make 2 or more pointers for operations.
#4.can only move forword, no backword traversing.
class Node:
    def __init__(self, info, next=None):
        self.data = info 
        self.next = next 

class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head 

    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else:
            self.head = temp  

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp  
#also used for searching
    def insertInMid(self, value, x):
        temp = Node(value)      
        t1 = self.head

        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next 
                t1.next = temp 
            t1 = t1.next

    #delete 
    def deleteLL(self, value):
        t1 = self.head 
        prev = t1 
        if(t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next 
                break
            else:
                prev = t1 
                t1 = t1.next 
        if(t1.data == value):
            prev.next = None

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data) 

obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertInMid(40, 20)
obj.deleteLL(30)
obj.printLL()
