class stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.insert(0, value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        return self.s[0]
    
    def pop(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        return self.s.pop(0)
    
    def length(self):
        return len(self.s)
    
    def get_all_elements(self):
        return self.s 

def main():
    stk = stack()
    while True:
        print("\n -- Stack CRUD Menu -- ")
        print("1.create/push")
        print("2.read/peek")
        print("3.update")
        print("4.delete/pop")
        print("5.exit !!!")
        choice = input("Enter the choice(1-5): ").strip()

        #create
        if choice == "1":
            item = input("Enter the item to push: ").strip()
            if item:
                stk.push(item)
                print(f"Item '{item}' pushed successfully.")
            else:
                print("Error: cannot add an empty item.")

        #read 
        elif choice == "2":
            if stk.length() == 0:
                print("The stack is currently empty")
            else:
                try:
                    print(f"\nTop element (peek): {stk.peek()}")
                except Exception as e:
                    print(e)
                print("\nCurrent stack items (Top to Bottom):")
                for i, item in enumerate(stk.get_all_elements()):
                    print(f"[{i}] {item}")

        #update 
        elif choice == "3":
            if stk.length() == 0:
                print("The stack is empty.")
                continue 
            try: 
                indx = int(input("Enter index of the item from top: "))
                if indx < 0 or indx >= stk.length():
                    raise IndexError 
                new_val = input("Enter the new value: ").strip()
                all_items = stk.get_all_elements() 
                old_val = all_items[indx]

                all_items[indx] = new_val
                print(f"updated '{old_val}' to '{new_val}'")
            except ValueError:
                print("Error: Enter a valid integer")
            except IndexError:
                print("Error: Index out of range")

        #delete 
        elif choice == "4":
            if stk.length() == 0:
                print("The stack is empty")
                continue 
            try:
                removed = stk.pop()
                print(f"popped '{removed}' from the top of the stack")
            except Exception as e:
                print(e)

        #exit 
        elif choice == "5":
            print("Exiting the program")
            break 
        else:
            print("Invalid Choice !!!")

if __name__ == "__main__":
    main()