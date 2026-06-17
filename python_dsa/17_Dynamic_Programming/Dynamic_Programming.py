# 0/1 Knapsack problem is solved using Dynamic Programming (DP)  
# because the naive recursive approach leads to exponential time complexity.
# dynamic programming makes time complexity(exponential -> polynomial)
# when no recursion and dynamic programming --> if many cases can be use & memoization technique
# recursion = high time complexity 
# dynamic programming = less time complexity

def knapsackDP(wt, value, capacity):
    n = len(wt)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(1, capacity+1):
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + value[i-1])
                #max(exclude, include) + profit 
            else:
                dp[i][w] = dp[i-1][w]
    print("Max Profit is", dp[n][capacity])

weights = [2,3,4,5]
values = [3,4,5,6]
knapsackDP(weights, values, 5)