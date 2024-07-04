# List is a collection which is ordered and changeable. 
# Allows duplicate members.
values = [1,2,3]
values[0] = 21
values.append(4)

# Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
values = (1,2,3)
# We cannot add / remove items in a tuple, & you cannot change existing values

# Set is a collection which is unordered, unchangeable*, and unindexed. 
# No duplicate members.
# *unchangeable: We can still add, remove elements in a set
values = {1,2,3}
print(type(values))
print(values)

# Add / Removing Items in a set
values.add(4)
print(values)

values.remove(4)
print(values)

values.discard(11)
print(values)

# No Duplicate
values.add(4) # should work
values.add(4) # is a duplicate
values.add(4) # is a duplicate
values.add(4) # is a duplicate
values.add(4) # is a duplicate
print(values)

# Helper Functions
values.clear()
print(values)

# Shallow copy in Sets
set_1 = {1,2,3}
set_2 = set_1

set_1.add(4)

# Deep Copy
set_3 = set_1.copy()

set_1.add(5)

# Pop
print(set_1) # 1 2 3 4 5
element = set_1.pop() # removes & return any random value from the set
print(element)
print(set_1)

# Finding an element
# in terms of speed SET(fastest) > TUPLE > LIST(slowest)
a = [1,2,3]
b = (1,2,3)
c = {1,2,3}

if 3 in c:
    print('3 found in the set')

if 3 in b:
    print('3 found in the tuple')

if 3 in a:
    print('3 found in the list')



# Set Operations
s1 = {1,2,3,4}
s2 = {4,5,6}

# Union: Adding sets together, Like a full/outter join
s3 = s1.union(s2) # 1 2 3 4 5 6
s3_ = s2.union(s1) # same as s3
print(s3)
print(s3_)

# Intersection: Finding Common Values between two sets, Like a inner join
s4 = s1.intersection(s2) # 4
s4_ = s2.intersection(s1) # same as s4
print(s4)

# Difference: Like right or left
s5 = s1.difference(s2) # {1,2,3,4} - {4,5,6} = {1,2,3}
print(s5)
s6 = s2.difference(s1) # {4,5,6} - {1,2,3,4} = {5,6}
print(s6)

# List, Tuple, Set Interaction
print('\n- List, Tuple, Set Interaction -\n')

# List
l1 = [1,2,3]
l1 = list([1,2,3])

# Convert Tuple to a list
l1 = list((1,2,3))
print(l1)

# Convert Set to a list
l1 = list({1,2,3})
print(l1)

# Advantages
t1 = (1,2,3)
# t1[0] = 4 # not allowed, since tuples are immutable. TypeError: 'tuple' object does not support item assignment
l1 = list(t1)
l1[0] = 4
print(l1)

s1 = {1,2,3}
# we cannot loop a set, we cannot change values, there are not indexing
l1 = list(s1)
l1[0] = 4
print(l1)

# Tuples
t1 = (1,2,3)
t1 = tuple((1,2,3))

# Convert list to a Tuple
t1 = tuple([1,2,3])
print(t1)

# Convert Set to a Tuple
t1 = tuple({1,2,3})
print(t1)

# Set
s1 = {1,2,3}
s1 = set({1,2,3})

# Convert list to a set
s1 = set([1,2,3,3])
print(s1)

# Convert tuple to a set
s1 = set((1,2,3,4,5,5))
print(s1)


# Remove all the duplicate values from a list
print('\n- Remove all the duplicate values from a list -\n')
l1 = [1,2,3,2,4,4,5,1,2,4,6,5]

s1 = set(l1)
print(s1)
l1 = list(s1)
print(l1)

l1 = list(set(l1))
print(l1)

# without sets
l2 = []
for value in l1:
    if value not in l2:
        l2.append(value)

print(l2)