# Hashing can be done by two ways:- 
# 1.Seperate Chaining 
# 2.Linear Probing

# Time and space complexity:- O(1) 

# Hashable/Immutable:- (Nochange in value beacuse if change then hashing position well also change)
# 1.strings 
# 2.Integers 
# 3.Tuples  

# Not Hashable/Mutable 
# 1.Arrays 
# 2.Dictionaries 
# .......

# Hashsets 

s = set()
print(s)

# Add items into set - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup if item in set - O(1)
if 1 not in s:
    print(True)

# Remove item from set - O(1)
s.remove(3)
print(s)

# Set construction - O(5) - 5 is the length of the string
string = "aaaaaaabbbbbbbbbbbbcccccccceeeeeeeee"
sett = set(string) 
print(sett)

# Loop over items in set - O(n)
for x in s:
    print(x)

#Hashmaps - Dictionaries
d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)

#Add key:val in dictionary: O(1)
d['arsh'] = 4 
print(d)

# Check for presence of key in dictionary: O(1)
if 'greg' not in d:
    print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'key {key}: val {val}')

# Defaultdict - eliminates KeyError exceptions
from collections import defaultdict 
default = defaultdict(int)
print(default[2]) # {2, 0}

from collections import defaultdict 
default = defaultdict(list)
print(default[2]) # {2, []}

# Counter - counts every occurance of values
from collections import Counter 
counter = Counter(string)
print(counter) 