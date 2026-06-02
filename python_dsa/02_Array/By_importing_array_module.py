# Array - two types 
# 1.Homogeneous - same datatypes
# 2.Heterogenous - different datatypes 
#3.fixed size - no addition after size full
#properties - 
#1.contigUous
#2.similar types of data (homo in c, c++,... etc,.)

#python implementation in two ways-
#1.Python array module 
#2.python numpy module 

#typecodes - 
'''
i == int == 2 byte 
w == unicode character == 2 byte
f == float == 4 byte 
d == float == 8 byte
'''




#By import array as arr #alias array as arr 
from array import *

#only homogenous array it create.
#but we cannot make 2d or 3d array in this method.

#val = arr.array('i',[1,2,3,4,5,6])
#val = array('d',[1,2,3,4,5,6,7,8,9,9.5]) # d = float

#val = array('w',['a','b','c'])  # w = characters
#for i in range(0, len(val)):
    #print(val[i], end=" ")

#print('\n')
#preferred to use loop this lower way
#for x in val:
    #print(x, end=" , ")

#print('\n')

#print(val.typecode)

#reverse an array 
#val.reverse()
#for i in range(0, len(val)):
    #print(val[i], end=" ")

#val = array('i',[1,2,3,4,5,6,7,8,9])

# update an array

# val.insert(1, 50)      # insert(index, value)
# val.append(100)    # add element at last
# val[2] = 200         #overwrite the data over index

#copyArray = array(val.typecode, (x*2 for x in val)) # (x*2) as a list me one by one store hoga

# for i in range(0, len(copyArray)):
#     print(copyArray[i], end=" ")    #shifing of elements takes place 

#delete an array

#copyArray.pop() # delete the element indexwisely or () - empty to delete last element 
#copyArray.remove(16)  #if want to delete actual element by name
# for i in range(0, len(copyArray)):
#     print(copyArray[i], end=" ")

#Array Slicing

#abc = val[2 : 5]   #[start index : end index]
# abc = val[2: -3]    #agar last se slicing 
# abc = val[::-1]     #to reverse using slicing
# for i in range(0, len(abc)):
#     print(abc[i], end=" ")

#taking input from user -- 
# arr = array('i', []) # i is typecode
# n = int(input("Enter a number: "))
# for i in range(0, n):
#     arr.append(int(input("Enter next input: ")))

# for x in arr:
#     print(x, end=" ")

# search an element in array

# arr = array("i", [12, 23, 45, 234, 134, 235])

# i = arr.index(134)
# print(i)
