#insertion - at rear(end).
#deletion - at front.
#note - insert/delete cannot be at middle.
#Queue ke bich ke elements nahi dhek sakte hain (😉by other person) in memory aur na hi access kiya ja sakta hai.

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):  #check underflow
        return len(self.items) == 0 
    
    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()

