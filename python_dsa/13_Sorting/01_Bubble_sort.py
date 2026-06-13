# iteration -- loop -- repeat again and again. i = (0 -> n-1)
# swaping (a,b = b,a)
# time complexity = O(n**2)
# increase order sorting
def bubbleSort(a):
    n = len(a)

    for i in range(n):                       # iteration
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]  # swaping

a = [64, 32, 25, 45, 40, 51, 2]
bubbleSort(a)
print(a) 
