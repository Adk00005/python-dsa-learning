# Heaps/priority queues 
# heapify = operation to create or repair heap tree-based data structure
# heapify = make min heap
# types:- 1. Min heap 2. Max Heap 
# nodes = lower value are roots with high priority
# heap tree properties:- 
# 1. lowerest node value == root 
# 2. highest node value == leaf 
# 3. not like binary search tree, as it is binary heap tree
# height of try = O(log N base 2)
# Time Complities:- 
# 1.Heap pop: O(logn)
# 2.Heap push: O(logn)
# 2.Heap peek: O(1)
# 3.Heap sort: O(nlogn)  -- best 
# space complexity:- O(1)
# Min Heap:- Heapify time complexity: O(n), space Complexity: O(1)

# Max heap:- node with higher value at top (root) and less value at (leaf of its root) 
# heaps are healpful to store data in tuples in python like min heap...

#_________________________________________________
# Build Min heap (Heapify)
# Time:O(n), space: O(1)
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
import heapq 
heapq.heapify(A)
print(A) 

# Heap Push (Insert element)
# Time: O(logn)

heapq.heappush(A, 4)
print(A) 

# Heap Pop (Extract min)
# Time: O(logn)

minn = heapq.heappop(A)
print((A, minn)) 

# Heap Sort 
# Time: O(nlogn), space: O(n)
# Note: O(1) space is available via swapping, but this is complex
def heapsort(arr):
    heapq.heapify(arr) 
    n = len(arr)
    new_list = [0] * n  
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn 
    return new_list 
print("Heap Sort:- ",heapsort([1, 2, 3, 4, 5, 6, 7, 8, 0]))

# Heap push pop:- Time: O(logn)
heapq.heappushpop(A, 99) # push 99 and pop the smallest(-4)
print(A)

# peek at min: Time(1)
print(A[0])

# Max Heap 

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range(n):
    B[i] = -B[i] # convert min heap to max heap
heapq.heapify(B)
print(B)

largest = -heapq.heappop(B)
print(largest)

heapq.heappush(B, -7) 
print(B)

# heap heap from scratsh:- Time: O(nlogn)
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap)) #check size of heap



# Leetcode problem - putting tuples of items on the heap 
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
from collections import Counter  
counter = Counter(D)
print(counter) # numbers the element occurs 

heap = []
for k, v in counter.items():
    print(heapq.heappush(heap, (v, k)))
print(heap)

