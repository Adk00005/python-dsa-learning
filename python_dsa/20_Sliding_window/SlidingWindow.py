# solved using two pointers (L,R)

# finding length of longest substring 
def lengthOfLongestSubstring(s: str) -> int:
    l = 0 
    longest = 0 
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1 
        w = (r - l) + 1 
        longest = max(longest, w) 
        sett.add(s[r])
    return longest 
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# time complexity: O(n)
# space complexity: O(n)


# Maximum Average subarray
from typing import List
def findMaxAverage(nums: List[int], k:int) -> float:
    n = len(nums)
    curr_sum = 0 
    for i in range(k):
        curr_sum += nums[i]
    max_avg = curr_sum / k

    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[k-i]

        avg = curr_sum / k 
        max_avg = max(max_avg, avg)
    return max_avg 
print(findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4))
# Time Complexity:- O(n)
# Space Complexity:- O(1)