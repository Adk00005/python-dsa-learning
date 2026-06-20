# Many ways to solve backtracking:- 
# using recursion, iteration, memoization/dynamic programming
# most commonly we used dfs technique to move in depth of all possible solutions
# here we use recursion --
# Recursive Backtracking
from typing import List    
def subsets(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    result, sol = [], []
    def backtrack(i):
        if i == n:
            result.append(sol[:])
            return
        # Don't pick arr[i]
        backtrack(i+1)
        # pick arr[i]
        sol.append(arr[i])
        backtrack(i+1)
        sol.pop()
    backtrack(0)
    return result 
arr = [1,2,3]
print(subsets(arr))
# time complexity: O(n**2)
# space complexity: O(n)

         
