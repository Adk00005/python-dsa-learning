class CircularQuene:
    def __init__(self, size):
        self.size = size 
        self.items = [None]*size 
        self.front = self.rear = - 1 

    #Create(Enqueue)
    def enqueue(self, value):
        if(self.rear + 1) % self.size == self.front:
            print("queue is full")
        elif self.front == -1:
            self.front = self.rear = 0 
            self.items[self.rear] = value 
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value 

    #delete(Deqeue)
    def deqeue(self):
        if self.front == -1:
            return None 
        removed = self.items[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1 

        else:
            self.front = (self.front + 1)  % self.size 
        return removed 
    
size = int(input("Enter circular queue size: "))
cq = CircularQuene(size)

def main():
    while True:
        print("\n --- python circular queue CRUD Menu ---")
        print("1.create")
        print("2.read")
        print("3.update")
        print("4.delete")
        print("5.exit")
        choice = input("Enter the choice(1-5): ")

        #create 
        if choice == "1":
            item = input("Enter item to enqueue/create: ")
            cq.enqueue(item)

        #read 
        elif choice == "2":
            if cq.front == -1:
                print("queue is empty")
            else:
                print("current circular queue:")
                i = cq.front 
                while True:
                    print(f"[{i}] : {cq.items[i]}")
                    if i == cq.rear:
                        break 
                    i = (i+1) % cq.size

        #update 
        elif choice == "3":
            try:
                index = int(input("Enter index to update: "))
                if index < 0 or index >= cq.size:
                    raise IndexError 
                if cq.items[index] is None:
                    print("No element present at this index")
                else:
                    old_val = cq.items[index]
                    new_val = input("Enter the new value: ")
                    cq.items[index] = new_val
                    print(f"updated '{old_val}' to '{new_val}'")
            except (ValueError, IndexError):
                print("Error: Invalid index.") 

        #delete 
        elif choice == "4":
            removed = cq.deqeue()
            if removed is None:
                print("queue is empty")
            else:
                print(f"removed '{removed}' from queue")

        #exit 
        elif choice == "5":
            print("exiting the program !!!")
            break

        else:
            print("Invalid choice, please try again")
if __name__ == "__main__":
    main()
