from numpy import * 

def main():
    data_array = array([])
    while True:
        print("\n -- Numpy Array CRUD Menu")
        print("1.Create an Array")
        print("2.Read an Array")
        print("3.Update an Array")
        print("4.Delete an Array")
        print("5.Exit !!!")
        choice = input("Enter the choice (1-5): ").strip()
        
        #create
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                data_array = append(data_array, item)
                print(f"Item '{item}' added successfully.")
            else:
                print("Error: Cannot add an empty item.")
            
        #Read 
        elif choice == "2":
            if data_array.size == 0:
                print("The array is currently empty.")
            else:
                print("\n current array items: ")
                for i, item in enumerate(data_array):
                    print(f"[{i}] {item}")
                
        #update
        elif choice == "3":
            if data_array.size == 0:
                print("The array is empty. Nothing to update")
                continue
            try:
                indx = int(input("Enter Index of item: "))
                if indx < 0 or indx >= data_array.size:
                    raise IndexError 
                
                new_val = input("Enter the new value: ").strip()
                old_val = data_array[indx]

                data_array[indx] = new_val 
                print(f"updated '{old_val}' to '{new_val}'")
            except ValueError:
                print("Error: enter value integer")
            except IndexError:
                print(f"Error: Index out of range")
        
        #delete
        elif choice == "4":
            if data_array.size == 0:
                print("the array is empty.")
                continue 
            try:
                indx = int(input("Enter the index"))
                if indx<0 or indx>= data_array.size:
                    raise IndexError
                
                removed = data_array[indx]
                data_array = delete(data_array, indx)
                print(f"removed '{removed}' from index {indx}.")
            except ValueError:
                print("Error: Invalid value")
            except IndexError:
                print("Error index out of range")

        #exit 
        elif choice == "5":
            print("Exiting to program")
            break 
        else:
            print("Invalid choice !!!")

if __name__ == "__main__":
    main()