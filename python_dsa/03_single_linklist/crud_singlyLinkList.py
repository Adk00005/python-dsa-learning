class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkList:
    def __init__(self):
        self.head = None 
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node # if head not present
        else:
            current = self.head  # if head present
            while current.next:
                current = current.next  
            current.next = new_node 
        self.size += 1

    def update(self, index, new_data):
        current = self.head 
        # Traverse exactly to target node 
        for i in range(index):
            current = current.next 
        old_val = current.data 
        current.data = new_data
        return old_val 
    
    def delete(self, index):
        if index == 0:
            removed = self.head.data 
            self.head = self.head.next
        else:
            current = self.head  
            #stop right before the node we want to delete 
            for i in range(index-1):
                current = current.next
                removed = current.next.data 
                current.next = current.next.next
        self.size -= 1 
        return removed 


def main():
    llist = LinkList()
    while True:
        print("\n -- Linked List CRUD Menu -- ")
        print("1.Create a LinkList")
        print("2.Read a LinkList")
        print("3.Update a LinkList")
        print("4.Delete a LinkList")
        print("5.Exit !!!")
        choice = input("Enter your desired (1-5) choice: ").strip()

        #Create
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                llist.append(item)
                print(f"Item '{item}' added successfully.")
            else:
                print("Error: Cannot add an empty item.")
        #Read 
        elif choice == "2":
            if llist.size == 0:
                print("The LinkList is currently empty.")
            else:
                print("\n current list items: ")
                current = llist.head 
                idx = 0 
                while current:
                    print(f"[{idx}] {current.data}")
                    current = current.next 
                    idx += 1 

        #Update 
        elif choice == "3":
            if llist.size == 0:
                print("The lsit is empty. Nothing is update.")
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
                print("Error: Out of Index !!")

        #Delete
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
                print("Error: Invalid value.")
            except IndexError:
                print("Error: Index Out of range.")
        #Exit 
        elif choice == "5":
            print("Exiting Program !!!")
            break
        else:
            print("Invalid Choice !!")


if __name__ == "__main__":
    main()
        