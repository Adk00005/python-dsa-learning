#Function calling itself is called recursion.
#breaking down of big problem into many smaller problems then solve it. 
#To build logic :- first catch (base case) - the smallest case whose answer you know very well.
# write base condition/terminating condition at first, otherwise trapped infinite loop.

#factorial code
def factorial(n):
    if n == 0 or n == 1:      #terminating condition
        return 1 
    return n * factorial(n-1) #recursion 
print(factorial(4))           #function calling

#fibonacci series code 
def fibonacci(n):
    if n == 1 or n == 2:      #terminating condition
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)  #recursion
print(fibonacci(4))           #function calling