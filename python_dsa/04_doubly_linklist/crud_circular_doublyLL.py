class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 

class CircularDoublyLinkList:
    def __init__(self):
        self.head = None 
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
            new_node.next = self.head 
            new_node.prev = self.head 
        else:
            tail = self.head.prev  #for last node
            tail.next = new_node 
            new_node.prev = tail 
            new_node.next = self.head 
            self.head.prev = new_node 
        self.size += 1 

    def update(self, index, new_data):
        current = self.head 
        for i in range(index):
            current = current.next  #pointer move each time
        old_val = current.data 
        current.data = new_data 
        return old_val   #contains new_val block into it, used later
    
    def delete(self, index):
        current = self.head 

        #if only one node in the list 
        if self.size == 1:
            removed = self.head.data 
            self.head = None 

        #delete head node if size > 1 
        elif index == 0:
            removed = self.head.data 
            tail = self.head.prev 
            self.head = self.head.next 
            self.head.prev = tail 
            tail.next = self.head 

        #delete mid or last node
        else:
            for i in range(index):
                current = current.next 
            removed = current.data 
            current.prev.next = current.next 
            current.next.prev = current.prev 

        self.size -= 1 
        return removed 
    
def main():
    llist = CircularDoublyLinkList()
    while True:
        print("\n -- Circukar Doubly Linked List CRUD Menu -- ")
        print("1.create") 
        print("2.read(traverse)") 
        print("3.update") 
        print("4.delete") 
        print("5.exit") 
        choice = input("Enter the choice(1-5): ").strip()

        #create 
        if choice == "1":
            item = input("Enter the item to add/create: ")
            if item:
                llist.append(item)
                print(f"item '{item}' added successfully.")
            else:
                print("Error: cannot add an empty item.")

        #read(traverse)
        elif choice == "2":
            if llist.size == 0:
                print("The linklist is currently empty.")
            else:
                #traverse forword
                print("\n Current list items (forword traversal): ")
                current = llist.head 
                for idx in range(llist.size):
                    print(f"[{idx}] {current.data}", end = "")
                    if idx < llist.size - 1:
                        print(" <--> ", end="")
                    current = current.next 
                print(" <--> (back to haed)")

                # traverse backward using circular tail
                print("\nVerification (Backward Traversal):")
                last_node = llist.head.prev #get tail node directly
                for idx in range(llist.size):
                    print(f"{last_node.data}", end="")
                    if idx < llist.size - 1:
                        print(" <--> ", end="")
                    last_node = last_node.prev 
                print(" <--> (back to tail)")
        
        #update
        elif choice == "3":
            if llist.size == 0:
                print("The list is empty")
                continue 
            try:
                indx = int(input("Enter index of the item: "))
                if indx < 0 or indx >= llist.size:
                    raise IndexError
                new_val = input("Enter the new value: ").strip()
                old_val = llist.update(indx, new_val) # retutn old_val on upper code
                print(f"updated '{old_val}' to '{new_val}'")
            except ValueError:
                print("Error: Invalid Integer !!")
            except IndexError:
                print("Error: out of range!!")
        
        #delete 
        elif choice == "4":
            if llist.size == 0: 
                print("The list is empty.")
                continue 
            try:
                indx = int(input("Enter the index: "))
                if indx < 0 or indx >= llist.size:
                    raise IndexError
                removed = llist.delete(indx)
                print(f"Removed '{removed}' from index '{indx}'")
            except ValueError:
                print("Error: Invalid value")
            except IndexError:
                print("Error: Indx out of range")

        #exit 
        elif choice == "5":
            print("Exiting the program !!!")
            break
        else:
            print("Invalid choice !!")


if __name__ == "__main__":
    main()