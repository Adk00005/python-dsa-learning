# two index variables (the "pointers") to traverse a linear data structure like a list or a string
# changes time complexity O(n**2) to O(n) using two pointers 
# abs = build-in function = removes negative of value, returns only magnitude
# Two Pointers Problem ----->

# sorted_squares
from typing import List
def sorted_squares(arr: List[int]) -> List[int]:
    left = 0            # Left Pointer 
    right = len(arr)-1  # Right Pointer
    result = []
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1 
        else:
            result.append(arr[right] ** 2)
            right -= 1 
    result.reverse()
    return result 
arr = [-4, -1, 0, 3, 10]
print(sorted_squares(arr))  
     