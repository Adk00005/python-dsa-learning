data_dict = {}

def main():
    global data_dict
    
    while True:
        print("\n --Now Take a look of (CRUD) at the menu my child--")
        print("1.create a Dictionary")
        print("2.read the Dictionary")
        print("3.update the Dictionary")
        print("4.delete the Dictionary")
        print("5.exit the Dictionary")
        choice = input("Hit an option: ")

        #1.create
        if choice == "1":
            key = input("Enter the key of dict: ")
            val = input("Enter the value of dict: ")
            data_dict[key] = val 
            print(f"success: Added {{{key}:{val}}}")
        
        #2.create
        elif choice == "2":
            if not data_dict:
                print("your Dictionary is empty")
            else:
                for key, val in data_dict.items():
                    print(f"key: {key} | value: {val}")
        
        #3.update
        elif choice == "3":
            try:
                key = input("Enter the key to update: ")
                if key in data_dict:
                    new_val = input(f"Enter the new value for {key}: ")
                    data_dict[key] = new_val
                    print("value Updated!")
                else:
                    print(f"Error key: {key} does not exist")
            except (ValueError,IndexError):
                print("Errror Orrured")
            
        #4.delete 
        elif choice == "4":
            try:
                key = input("Enter the key to delete: ")
                removed = data_dict.pop(key, None) #.pop() removes the key and returns None if it doesn't exist, preventing crashes
                if removed is not None:
                    print(f"Deleted key: {key}")
                else:
                    print(f"Error key: {key} not found")
            except (ValueError, IndexError):
                print()
        
        #5.exit
        elif choice == "5":
            print("Exiting the program!!!!")
            break
        else:
            print("Invalid choice !! choice from the given options my child")


if __name__ == "__main__":
    main()