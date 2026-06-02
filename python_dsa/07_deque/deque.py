#insertion - at rear(end) or at beginning.
#deletion - at front or at rear.
#note - insert/delete cannot be at middle.
#iske ke bich ke elements nahi dhek sakte hain (😉by other person) in memory aur na hi access kiya ja sakta hai.

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):  #check underflow
        return len(self.items) == 0 
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop()

dq = Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
dq.deleteAtEnd()
dq.deleteAtFront()
