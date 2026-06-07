# ---- Tree Traversal ----

#        |_1_|  -> root node(Root) 
#         /  \
#        /    \
#    |_2_|   |_3_|  -> leaf node 
#     (L)     (R)
# 
# 1 -> 2 -> 3 = Preorder(Root->L->R)
# 2 -> 1 -> 3 = Inorder (L->Root->R)
# 2 -> 3 -> 1 = postorder(L->R->Root)

class Node:
    def __init__(self, value):  #constructor
        self.left = None 
        self.right = None 
        self.data = value 

def preOrder(root):
    if root != None:
        print(root.data, end = " ")
        preOrder(root.left)
        preOrder(root.right) 

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end = " ")
        InOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end = " ")


root = Node(1)
root.left = Node(3)
root.right = Node(5)

root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)
preOrder(root)
InOrder(root)
postOrder(root)

#Note :- This is not a BST.