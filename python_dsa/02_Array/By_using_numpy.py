from numpy import * #numpy allows 2d and 3d array making.

# val = array([1,2,4.5,'a']) # no typecode required in numpy method.
# #numpy - hetrogenous array it create
# for x in val:
#     print(x, end=" ")

# val = array([1,2,4], float) #with typecode like that
# for x in val:
#     print(x, end=" ")

#Linspace
#val = linspace(10, 20, 11)  #make arithmatic progression
#divides in 11 equal parts from 10 to 20 including both
#for x in val:
#    print(x, end=" ")

#arange
# val = arange(10,20,2) # gap of 2 array like 10+2,...
# 10 include but 20 not include
# for x in val:
#     print(x, end=" ")

#using log in maths 
# val = logspace(10,20,2)
# for x in val:
#     print(x, end=" ")

# numbers arrray using zeros, ones, ... etc
# val = ones(10)
# for x in val:
#     print(x, end=" ")

# repeat same numbers using full
# val = full(10,5)  #(total array size, number to repeat)
# for x in val:
#     print(x, end=" ")

#you can use reverse, ....etc,.

#Multidimentional Array 

zero = array(10) #zero dimentional array 
#print(zero)

one = array([1,2,3,4,5]) #two dimentional array
#print(one)

two = array([[1,2,3], [4,5,6], [7,8,9]]) #two dimentional array 
#print(two)

three = array([ [[1,2], [3,4]], [[5,6], [7,8]] ])  #three dimentional array
#each three dimentional array is a collection of two dimentional array
#each two dimentional array is a collection of one dimentional array
print(three)  #data in array should be of same length to equally distribute it.







