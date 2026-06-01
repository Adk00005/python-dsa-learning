class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 
    
class DoublyLinkList:
    def __init__(self):
        self.head = None 
        self.size = 0 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_node 
            new_node.prev = current 
        self.size += 1 

    def update(self, index, new_data):
        current = self.head 
        for _ in range(index):
            current = current.next 
        old_val = current.data 
        current.data = new_data 
        return old_val  
    
    def delete(self, index):
        current = self.head 

        #delete head node 
        if index == 0:
            removed = self.head.data 
            self.head = self.head.next 
            if self.head:
                self.head.prev = None 

        #delete middle or last node 
        else:
            for _ in range(index):
                current = current.next 
            removed = current.data 

            #disconnect the target node 
            current.prev.next = current.next 
            if current.next:
                current.next.prev = current.prev 
        self.size -= 1
        return removed 
    

def main():
    llist = DoublyLinkList()
    while True:
        print("\n -- Doubly Linked list CRUD Menu -- ")
        print("1.create")
        print("2.read")
        print("3.update")
        print("4.delete")
        print("5.exit")
        choice = input("Enter you (1-5) choice: ").strip()
        
        #create
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                llist.append(item)
                print(f"item '{item}' added successfully.")
            else:
                print("Error: cannot add an empty item.")

        #read 
        elif choice == "2":
            if llist.size == 0:
                print("The linklist is currently empty.")
            else:
                print("\nCurrent list items (Forword traversal):")
                current = llist.head
                idx = 0 
                last_node = None 
                while current:
                    print(f"[{idx}] {current.data}", end="")
                    if current.next:
                        print(" <--> ", end="")
                    last_node = current 
                    current = current.next 
                    idx += 1 
                print()

                #traversal backwards using prev pointers
                print("Verification (Backward Traversal):")
                while last_node:
                    print(f"{last_node.data}", end="")
                    if last_node.prev:
                        print(" <--> ", end="")
                    last_node = last_node.prev
                print()


        #update
        elif choice == "3":
            if llist.size == 0:
                print("The list is empty. Nothing to update.")
                continue 
            try: 
                indx = int(input("Enter index of item: "))
                if indx < 0 or indx >= llist.size:
                    raise IndexError 
                new_val = input("Enter the new value: ").strip()
                old_val = llist.update(indx, new_val)
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
                print("Error: Index out of range")

        #exit 
        elif choice == "5":
            print("Exiting program !!!")
            break 
        else:
            print("Invalid choice !!")



if __name__ == "__main__":
    main() 