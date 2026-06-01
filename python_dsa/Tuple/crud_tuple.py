data_tuple = ()

def main():
    global data_tuple
    while True:
        print("\n--- python Tuple CRUD Menu ---")
        print("1. Create (Add Item)")
        print("2. Read (View All Items)")
        print("3. Update (Change Item)")
        print("4. Delete (Remove Item)")
        print("5. Exit")

        choice = input("Enter the choice(1-5): ")

        #1. create -- 
        if choice == "1":
            item = input("Enter the item to add: ")
            data_list = list(data_tuple)
            data_list.append(item)
            print(f"item: {item} added successfully.")
            data_tuple = tuple(data_list)

        #2. Read -- 
        elif choice == "2":
            if not data_tuple:
                print("The Tuple is currently empty.")
            else:
                print("current tuple items: ")
                for i, item in enumerate(data_tuple):
                    print(f"{i}: {item}")
        
        #3. Update --
        elif choice == "3":
            try:
                data_list = list(data_tuple)
                indx = int(input("Enter the index of the item to update: "))
                new_val = input("Enter the new value: ")
                old_val = data_list[indx]
                data_list[indx] = new_val 
                print(f"Updated '{old_val}' to '{new_val}' at index {indx}.")
                data_tuple = tuple(data_list)
            except (ValueError, IndexError):
                print("Error: Invalid index.")

        #4. Delete -- 
        elif choice == '4':
            try:
                data_list = list(data_tuple)
                indx = int(input("Enter the index to delete the item: "))
                removed = data_list.pop(indx)
                data_tuple = tuple(data_list) 
                print(f"Removed '{removed}' from index {indx}.")
            except (ValueError, IndexError):
                print("Error: Invalid Index.")
        #5. Exit -- 
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.") 

if __name__ == "__main__":
    main()



