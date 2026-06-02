class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, value):
        self.items.append(value)
    
    def delete(self):
        if self.isEmpty():
            return None 
        return self.items.pop(0)

q = Queue() 

def main ():

    while True:
        print("\n --- Python Queue CRUD Menu ---")
        print("1.create (Insert Items)") 
        print("2.read (view Queue)") 
        print("3.update (change items)") 
        print("4.delte (remove front item)") 
        print("5.exit")

        choice = input("Enter the choice (1-5): ")

        #create
        if choice == "1":
            item = input("Enter the item to insert: ")
            q.insert(item)
            print(f"item '{item}' inserted successfully")

        #read 
        elif choice == "2":
            if  q.isEmpty():
                print("queue is currently empty.")
            else:
                print("current queue:")
                for i, item in enumerate(q.items):
                    print(f"'[{i}]' : '{item}'")

        #update 
        elif choice == "3":
            try:
                indx = int(input("Enter the index to update: "))
                old_val = q.items[indx]
                new_val = input("Enter the new value: ")
                q.items[indx] = new_val 
                print(f"updated '{old_val}' to '{new_val}'.")
            except (ValueError, IndexError):
                print("Error: Invalid position")

        #delete
        elif choice == "4":
            removed = q.delete() 
            if removed is None:
                print("queue is empty.")
            else:
               print(f"removed '{removed}' from the queue.") 

        #exit 
        elif choice == "5":
            print("exiting program !!!")
            break 
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()