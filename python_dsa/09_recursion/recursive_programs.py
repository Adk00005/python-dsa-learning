#1.sum of N Numbers 
def sum_n(n):
    if n == 1:              #terminating condition
        return 1
    return n + sum_n(n-1)   #recursion

n = int(input("Enter the number: "))
print("Sum = ", sum_n(n)) 

#2.reverse a string 
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

text = input("Enter the string: ")
print("Reversed string:", reverse_string(text))

#3.palindrome check  
def is_palindrome(s):
    if len(s) <= 1:
        return True 
    if s[0] != s[-1]:
        return False 
    return is_palindrome(s[1:-1])

text = input("Enter s string: ")
if is_palindrome(text):
    print("palindrome")
else:
    print("Not palindrome")

#4.Binary Search Using Recursion
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, high, target)


arr = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Found at index", result)
else:
    print("Not Found") 

#5.towar of hanoi 
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move Disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print(f"Move Disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, "A", "B", "C")

#6.recursion on arrays 
def print_array(arr, index):
    if index == len(arr):
        return  
    print(arr[index])
    print_array(arr, index+1)
arr = [10, 20, 30, 40, 50]
print_array(arr, 0)

#7.recursion on arrays(find sum)
def array_sum(arr, index):
    if index == len(arr):
        return
    return arr[index] + array_sum(arr, index + 1)

arr = [10, 20, 30, 40, 50]
print("Sum: ", array_sum(arr, 0))

#8.Backtracking Basics (Generate All Binary Strings)
def generate_binary(n, current=""):
    if len(current) == n:
        print(current)
        return

    generate_binary(n, current + "0")
    generate_binary(n, current + "1")


n = int(input("Enter length: "))

generate_binary(n)

