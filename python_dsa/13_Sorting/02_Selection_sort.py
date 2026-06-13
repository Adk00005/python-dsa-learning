# selection sort 2 approach - 1. find smallest and then swap over first position.and
#                             2. find largest and then swap over last position.
# time complexity - O(n**2)

# using 1st approach--
def SelectionSort(a):
    n = len(a)
    
    for i in range(n):
        min = i 
        for j in range(i, n):
            if (a[min] > a[j]):
                min = j 
        a[i], a[min] = a[min], a[i]

a = [64, 32, 25, 45, 40, 51, 2]
SelectionSort(a)
print(a) 