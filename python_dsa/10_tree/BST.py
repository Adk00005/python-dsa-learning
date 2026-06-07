#Binary Tree != Binary search tree
# Time Complexity BT = O(n)
# Time Complexity BST = O(logn) -- fast
# BT Properties :- 1. Atmost 2 child. 
# BST Properties :- 1. Root left side < Root
#                   2. Root right side < Root  
#                   3. height = logn

# Interview questions on BST - 
# |-> 1.Print all elements of BST in increasing order.
# |-> 2.How to check a valid BST.
# |-> 3.Inorder Traversal of BST. 
# ***All Questions are same***
# valid BST = increasing order = inorder traversal follows 
# hence to check valid BST it is in increasing order

#Time Complexity :- insertion single element = O(logn)
#                   insertion many element = O(nlogn)
#Time Complexity :- searching = O(logn)          


class Node:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.data = value 

#Insertion
def insert(root, value):
        if root == None:
            return Node(value)
        if root.data == value:
            return root 
        if root.data > value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value) 
        return root

#searching
def search(root, value):
        if root == None:
            print("Element not found", end="\n")
            return 
        if root.data == value:
            print("Element found", end="\n") 
            return 
        if root.data > value:
            search(root.left, value)
        else:
            search(root.right, value) 
        

# **----- Deletion in BST-----**

# 1.Inorder Successor = One step towards right and then leftmost element.
# 2.Inorder Predessor = One step towards left and then rightmost element.

def get_successor(root):
        root = root.right
        while(root != None and root.left != None):
          root = root.left
        return root


#cases of deletion :-

# case 1:- Deletion of leaf(0 child) = too us node ke parent node ka address pata hona chaiye.
# case 2:- Deletion of node having 1 child = deleted node ke child ko after deletion, deleted node ke parent se direct connect kar denge.
# case 3:- Deletion of node having 2 child = use inorder predessor/successor then connect the child node of deleted node with deleted node parent.

#deletion
def delete(root, value):
        if root == None:
            return root
        elif root.data > value:
             root.left = delete(root.left, value)
        elif root.data < value:
             root.right = delete(root.right, value)
        else:
             if root.left == None:
                  return root.right
             if root.right == None:
                  return root.left
             else:
                  succ = get_successor(root)
                  root.data = succ.data
                  root.right = delete(root.right, succ.data) # deleted node ke parent ka address hona hi chaiye
        return root

#read
def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end = " ")
        InOrder(root.right)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

InOrder(root) #increasing order me BST print kar ke dega

search(root, 18)
search(root, 100)

delete(root, 30)
print("\n")
InOrder(root)



