# bst me parents node ka address pata hona bhut jaruri hai 

class Node:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.data = value 

class BST:

    def __init__(self):
        self.root = None 

    #create(Insert)
    def insert(self, root, value):
        if root is None:
            return Node(value)
        elif root.data == value:
            return root 
        elif root.data > value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root 
    
    #read(Inorder Traversal)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    #search
    def search(self, root, value):
        if root is None:
            return False
        elif root.data == value:
            return True
        elif root.data > value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)
        
    #Inorder successor
    def get_successor(self, root):
        root = root.right 
        while root is not None and root.left is not None:
            root = root.left 
        return root
    
    #delete
    def delete(self, root, value):
        if root is None:
            return root 
        elif root.data > value:
            root.left = self.delete(root.left, value)
        elif root.data < value:
            root.right = self.delete(root.right, value)
        else:
            # node with 0 or 1 child
            if root.left is None:
                return root.right 
            if root.right is None:
                return root.left 
            else:
                # node with 2 child
                succ = self.get_successor(root)
                root.data = succ.data 
                root.right = self.delete(root.right, succ.data)
        return root

    #update 
    def update(self, old_value, new_value):
        if self.search(self.root, old_value):
            self.root = self.delete(self.root, old_value)
            self.root = self.insert(self.root, new_value)
            print(f"Updated {new_value} to {old_value}")
        else:
            print("Value not found.")

bst = BST()

def main():
    while True:
        print("\n --- Python BST CRUD Menu ---")
        print("1.create/insert")
        print("2.read(Inorder Traversal)")
        print("3.update")
        print("4.delete")
        print("5.search")
        print("6.exit")
        choice = input("Enter choice (1-6): ")

        #create 
        if choice == "1":
            value = int(input("Enter the value: "))
            bst.root = bst.insert(bst.root, value)
            print(f"{value} inserted successfully.")

        #read 
        elif choice == "2":
            if bst.root is None:
                print("BST is empty.")
            else:
                print("BST elements: ")
                bst.inorder(bst.root)
                print()
        
        #update
        elif choice == "3":
            old_value = int(input("Enter value to update: "))
            new_value = int(input("Enter new value: "))
            bst.update(old_value, new_value)
        
        #delete
        elif choice == "4":
            value = int(input("Enter the value to delete: "))
            bst.root = bst.delete(bst.root, value)
            print(f"{value} is deleted successfully.")

        #search
        elif choice == "5":
            value = int(input("Enter the value to search: "))
            if bst.search(bst.root, value):
                print("Value found.")

        #exit
        elif choice == "6":
            print("Exiting program !!!")
            break 
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

