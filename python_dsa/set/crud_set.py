data_set = set()

def main():
    global data_set
    while True:
        print("\n Python set CRUD menu")
        print("1.Create/Add the set")
        print("2.Read set data")
        print("3.Update set data")
        print("4.Delete set data")
        print("5.Exit the system")
        choice = input("Choose the option to start the operation: ")

        #1.create 
        if choice == "1":
            item = input("Enter the item to create/add over set: ")
            data_set.add(item)
        
        #2.read 
        elif choice == "2":
            if not data_set:
                print("set is empty")
            else:
                print("Current items in set: ")
                for i, item in enumerate(data_set):
                    print(f"{i}:{item}")
        
        #3.update
        elif choice == "3":
            try:
                data_list = list(data_set)
                indx = int(input("Enter the index no: "))
                new_val = input("Enter the item to update: ") 
                data_list[indx] = new_val
                data_set = set(data_list)
            except (ValueError, IndexError):
                print("Invalid Index!")

        #4.delete 
        elif choice == "4":
            try:
                data_list = list(data_set)
                indx = int(input("Enter the index no: "))
                data_list.pop(indx)
                data_set = set(data_list)
            except (ValueError, IndexError):
                print("Invalid number Entered!")

        #5.exit 
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

