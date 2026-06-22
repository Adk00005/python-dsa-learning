#1. Suffix Sum Program -- 
from typing import List 
def build_suffix_sum(nums:List[int]) -> List[int]:
    n = len(nums)
    suffix_sum = [0]*n
    current_sum = 0 
    for i in range(n-1, -1, -1):
        current_sum += nums[i]
        suffix_sum[i] = current_sum 
    return suffix_sum
nums = [10, 14, 16, 20]
print(build_suffix_sum(nums))
# Time Complexity:- O(n)
# Space Complexity:- O(n)

#2. String Suffix 
text = "Data Structures"

print(text.endswith("Structures"))

print(text[-10:])

clean_text = text.removesuffix("Structures")
print(clean_text)

#3. Suffix Array 
def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]  # list comprehension
    suffixes.sort(key=lambda x:x[0])
    return [original_index for suffix, original_index in suffixes]
text = "BANANA"
print(build_suffix_array(text))

# Time Complexity:- O(nlogn)
# Space Complexity:- O(n)