# 1. Two-Sum Pattern (Complement Lookup)
from typing import List 
def two_sum(nums: List[int], target) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index] 
        seen[num] = index
    return []
print(two_sum([2,7,11,15], 9))
# Time Complexity: O(n)
# Space Complexity: O(n)

# 2. Frequency Counting & First Unique Element Pattern
def first_unique_char(s: str) -> int:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1 
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index 
    return -1
print(first_unique_char('leetcode'))
# Time Complexity: O(n)
# Space Complexity: O(k), where k ->unique element

# 3. Grouping Items (Anagrams / Categorization)
# Two words are anagrams if they use the exact same characters in any order 
#  |->(e.g., "listen" and "silent" or "eat" and "tea")
def group_anagrams(strs: List[str]) -> List[str]:
    anagram_map = {}
    for s in strs:
        sorted_key = "".join(sorted(s))
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        anagram_map[sorted_key].append(s)
    return list(anagram_map.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Time Complexity: O(n-mlogm)
# Space Complexity: O(n-m)

# 4. Prefix Sum + Hash Map (Subarray Sum Equals K) 
def subarray_sum(nums: List[int], k: int) -> int:
    count = 0 
    current_sum = 0 
    prefix_sum = {0:1}
    for num in nums:
        current_sum += num 
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1 
    return count 
print(subarray_sum([1,2,3], 3))       
# Time Complexity: O(n)
# Space Complexity: O(n) 