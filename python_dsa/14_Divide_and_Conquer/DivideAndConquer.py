# Break 1 problem into many similar small problems then break it using recursion.
# Use "Recursion" very well
# write finding min, max in array using divide and conquer -
def find_min_max(arr, start, end):
    if start == end:
        return arr[start], arr[end]  # python return multiple value in the form of tuple
    elif start + 1 == end:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
    mid = (start + end) // 2 
    min1, max1 = find_min_max(arr, start, mid)
    min2, max2 = find_min_max(arr, mid+1, end)
    return min(min1, min2), max(max1, max2)
arr = [23,14,45,3,6,10]
min, max = find_min_max(arr, 0, len(arr)-1)
print("minimum value is:",min)
print("maximum value is:",max)