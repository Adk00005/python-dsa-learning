class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
       return len(self.items) == 0
    
    def insertAtFront(self, value):
        self.items.insert(0, value)

    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isEmpty():
            return None 
        return self.items.pop(0)
    
    def deleteAtEnd(self):
        if self.isEmpty():
            return None 
        return self.items.pop()
    
dq = Deque() 

def main():
    while True:
        print("\n--- python deque CRUD Menu ---")
        print("1.create/insert at front") 
        print("2.create/insert at front") 
        print("3.read/view deque") 
        print("4.update item") 
        print("5.delete at front")
        print("6.delete at end")
        print("7.exit")

        choice = input("Enter the choice(1-7): ")

        #create/insert at front 
        if choice == "1":
            item = input("Enter the item to insert at front: ")
            dq.insertAtFront(item)
            print(f"item '{item}' inserted at front successfully.")

        #create/insert at end 
        elif choice == "2":
            item = input("Enter the item to insert at end: ") 
            dq.insertAtEnd(item)
            print(f"item '{item}' inserted at end successfully.")
        
        #read/view deque 
        elif choice == "3":
            if dq.isEmpty():
                print("Deque is currently empty.")
            else:
                print("current deque:")
                for i, item in enumerate(dq.items):
                    print(f"[{i}] : '{item}'")

        #update 
        elif choice == "4":
            try:
                indx = int(input("Enter the index to update: "))
                old_val = dq.items[indx]
                new_val = input("Enter the new value: ")
                dq.items[indx] = new_val 
                print(f"updated '{old_val}' to '{new_val}' at index {indx}.")
            except (ValueError, IndexError):
                print("Error: Invalid index.")

        #delete at front 
        elif choice == "5":
            removed = dq.deleteAtFront()
            if removed is None:
                print("deque is empty.")
            else:
                print(f"removed '{removed}' from front.")

        #delete at end 
        elif choice == "6":
            removed = dq.deleteAtEnd()
            if removed is None:
                print("deque is empty.")
            else:
                print(f"removed '{removed}' from end.")

        #exit 
        elif choice == "7":
            print("Exiting the program !!!")
            break 

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()