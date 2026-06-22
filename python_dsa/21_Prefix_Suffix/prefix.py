# 1. prefix sum program--
from typing import List 
def prefixSum(arr: List[int]) -> List[int]:
    n = len(arr)
    prefix = [arr[0]]
    for i in range(1,n):
        prefix.append(prefix[-1] + arr[i])
    return prefix
arr = [5, 10, 30, 4, 5]
print(prefixSum(arr))

# Time Complexity:- O(n)
# Space Complexity:- O(n)

# optimized upper code 

def runningSum(nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i-1]
        return nums
nums = [5, 10, 30, 4, 5]
print(runningSum(nums))

# Time Complexity:- O(n)
# Space Complexity:- O(n)

#2. String Suffix --
text = "Data Structures"

print(text.startswith("Data "))

print(text[5:])

clean_text = text.removeprefix("Data ")
print(clean_text)

