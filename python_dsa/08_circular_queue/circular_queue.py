#circular queue is used due to the drawback of normal queue.
#normal queue insertion takes place at rear but even their's a space at front index in array, 
# you cannot add elements as it insert bydefault at end(rear) of it. 

#circular queue removes this normal queue drawback.
#no use of append or pop code but use front and rear pointer.

#consideration:- 
#1.(front = rear = -1) -- empty circular queue or to delete last element
#2.(front = rear = 0)  -- only one element in it
#3.insert => (rear = (rear + 1) % size) -- (enqueue) - on add an element 
#4.delete => (front = (front + 1) % size) -- (dequeue) - on delete an element
#5.((rear + 1) % size == front) -- check if full
class CircularQueue:
    def __init__(self, size):
        self.size = size 
        self.items = [None]*size # creates list of some mentioned size.
        self.front = self.rear = -1 

    #insertion
    def enqueue(self, value):
        if((self.rear + 1) % self.size == self.front):
            print("queue is full")
        elif self.front == -1:
            self.front = self.rear = 0 
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value 

    #deletion
    def dequeue(self):
        if(self.front == -1):
            print("queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1  
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
