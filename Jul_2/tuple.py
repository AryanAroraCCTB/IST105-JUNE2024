# Data Structure
# List is a collection which is ordered and changeable. 
# Allows duplicate members.

list = [1,2,3,3]
print(type(list))

list[0] # 1
list[3] # 3
list[3] = 4 # [1,2,3,4]


# Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
colors = ('green', 'blue', 'orange', 'orange')
print(type(colors))

print(colors[0])
print(colors[1])
print(colors[2])

# colors[3] = 'yellow' # unchangeable

# Properties of a tuple
# - Ordered
# - Indexed
# - Hetrogenous
fav = (1, 'two', 3.0)
fav = [1, 'two', 3.0]
# - Unchangeable = Immutable

# Tuples

# Creating Tuples
colors = ('green', 'blue', 'orange', 'orange')
colors[1] # blue

fav = (
    1, 
    'two', 
    3.0, 
    True, 
    [1,2,3], 
    ('green', 'blue', 'orange', 'orange')
)

print(colors[1]) # blue

some_list = fav[5]
print(
    (some_list)[1]
) # blue

print(
    (fav[5])[1]
) # blue

print(
    fav[5][1]
) # blue

# Helper Methods
# count
# index
colors = ('green', 'blue', 'maroon', 'orange', 'yellow', 'orange')
print(colors.count('orange'))

num = colors.index('orange') # 3
print(num)

num_2 = colors.index('orange', num+1) # 5
print(num_2)

# Add Tuples together
tuple_1 = ('green', 'blue', 'yellow')
tuple_2 = ('orange', 'maroon', 'red')
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

# Shallow copy on list vs tuple
c = ['green', 'blue', 'yellow']
d = c

print(d[1])
c[1] = 'orange'
print(d[1])

a = ('green', 'blue', 'yellow')
b = a

print(b[1])
# a[1] = 'orange' # VALUE ERROR: Since tuples are immutable
print(b[1])

# Repeat
tuple_1 = (1,2) * 2 # (1,2,1,2)

print('-----------------------')

# Looping List
colors = ['green', 'blue', 'maroon', 'orange', 'yellow', 'orange']


for color in colors:
    print(color)

index = 0
while(index < len(colors)):
    print(colors[index])
    index+=1

# Looping Tuple
colors = ('green', 'blue', 'maroon', 'orange', 'yellow', 'orange')

for color in colors:
    print(color)

index = 0
while(index < len(colors)):
    print(colors[index])
    index+=1