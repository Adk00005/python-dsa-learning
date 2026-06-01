class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class CircularLinkList():
    def __init__(self):
        self.head = None 
        self.size = 0 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
            new_node.next = self.head #points to itself initially
        else:
            current = self.head 
            # to add functionality by traverse - while loop
            while current.next != self.head:
                current = current.next 
            current.next = new_node 
            new_node.next = self.head 
        self.size += 1 

    def update(self, index, new_data):
        current = self.head 
        # to standard traversal use for loop 
        for i in range(index):
            current = current.next 
        old_val = current.data  
        current.data = new_data 
        return old_val 
    
    def delete(self, index):
        if index == 0:
            removed = self.head.data
            if self.size == 1:
                self.head = None  # list become empty
            else:
                last_node = self.head 
                while last_node.next != self.head:
                    last_node = last_node.next 
                    last_node.next = self.head #maintain circle
        else:
            current = self.head 
            #stop before the desired deletable node 
            for i in range(index - 1):
                current = current.next 
            removed = current.next.data
            current.next = current.next.next 
        
        self.size -= 1 
        return removed 
    
def main():
    llist = CircularLinkList()
    while True:
        print("\n -- Circular Linked List CRUD Menu -- ")
        print("1.create")
        print("2.read")
        print("3.update")
        print("4.delete")
        print("5.exit")
        choice = input("Enter your desired(1-5) choice: ")
        
        #create 
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                llist.append(item)
                print(f"Item '{item}' added successfully.")
            else:
                print("Error: cannot add an empty item.")

        #read
        elif choice == "2":
            if llist.size == 0:
                print("The linklist ti currently empty.")
            else:
                print("\n Current list items:")
                current = llist.head
                idx = 0
                #execution loop - while loop
                while True:
                    print(f"[{idx}] {current.data}")
                    current= current.next 
                    idx += 1
                    if current == llist.head:
                        break 

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
                print("Error: Index out of range !!")

        elif choice == "4":
            if llist.size == 0:
                print("The link is empty.")
                continue 
            try: 
                indx = int(input("Enter the index: "))
                if indx < 0 or indx >= llist.size:
                    raise IndexError
                removed = llist.delete(indx)
                print(f"Removed '{removed}' from index '{indx}'")
            except ValueError:
                print("Error: Invalid Value")
            except IndexError:
                print("Error: Index out of range")

        elif choice == "5":
            print("Exiting program !!!")
            break 
        else:
            print("Invalid choice !!")

if __name__ == "__main__":
    main()

