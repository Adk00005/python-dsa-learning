# Tree have 3 nodes - Root node, Intermediate node, leaf node.
# have levels (upper level - level 0) and then level 1 then level 2...
# leafs are siblings if they are at the same levels.
# the node which have child are called parent node.
# only (root node to leaf node) or we can say (parent to child node) traverse can possible.
# no leaf to root node or (parent to child node) traversal is possible.
# if want to backtrack traverse then use stack, or recursion.
# childs cannot communicate with each others.
# child use stack or recursion to backtrack to father node to communicate.
# even a single node can be called as tree.
# Types of tree:- 
#   1. Binary tree - each node max have 2 childs.
#   2. Binary search tree - (each left side node < right side node of tree)
#          |-> left node less than its father node
#          |-> right node higher than its father node
#   3. Strict/Full Binary tree - Exactly 0 or 2 child but no single child is allowed.
#   4. Complete Binary tree - (0, 1, 2)child allowed
#          |-> new node filling start from left most node otherwise its next right node.
#          |-> upper previous level must be full
#   5. Skew Binary tree - single node append only on one side 
#          |-> left skew binary tree
#          |-> right skew binary tree
#   6. Degenerated tree - single node append only on both side. 
#   7. Extended Binary tree - add dummy node as child on every leaf nodes.


#   Binary tree representation:- memory allocation manners for tree
#          |-> 1.Array - contigious
#          |-> 2.Linklist - non-contigious
#   logical view - tree 
#   physical view - array or linklist
#   Array logic:- Left child - {(index)*2 + 1} = left child
#                  Right child - {(index)*2 + 2} = right child
#                  where, index = index of parent node 
#                  use this when have complete binary tree, if not then make dummy nodes.
#   Drawback of array use :- wastage of memory 
#   Linklist Logic:- using Doubly linklist 
#                    No memory wastage and no dummy node creation required.


