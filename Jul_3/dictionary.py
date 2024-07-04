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
values = {1,2,3,3}
# print(type(values))
# print(values)

# Dictionary is a collection which is ordered** and changeable. 
# No duplicate members.
values = { 'key': 'value', 'key2': 'value2' }
values = { 'name': 'john', 'age': 25 }
values = dict({ 'name': 'john', 'age': 25 })
values = dict(name='john', age=25)

print(values)

# Accessing the dictionary using the keys
print(values['name'])
print(values['age'])

x = values['name']
print(x)
x = values.get('name')
print(x)

# Changing values based on the key
values['age'] = 22
print(values)

# Add keys-value pairs
values['phone'] = '7781234567'
print(values)

# Add multiple keys-value pairs
values.update({'last_name': 'smith', 'country': 'CANADA'})

# Remove an existing key-value pair
del values['phone']
print(values)

values.clear()
print(values)

# Dictionary like all the other collections, does a shallow copy
d1 = dict(name='john', age=25)

d2 = d1
d1['name'] = 'smith'

d2 = d1.copy()
d1['name'] = 'john'

# Methods
print('\n- Methods -\n')

# get all the keys
d1_keys = d1.keys() # name, age
print(d1_keys)

# get all the values
d1_values = d1.values()
print(d1_values)

# get key-value pair as list of tuples
d1_items = d1.items()
print(d1_items)

# Iterating the dictionary
print('\n- Iterating the dictionary -\n')

# similar to the list for loop
l1 = [1,2,3]
for value in l1:
    print(value)

keys = d1.keys() # ['name', 'age']
values = d1.values() # ['john', '25']
items = d1.items() # [ ('name', 'john'), ('age', 25) ]

for key in keys:
    value = d1[key]
    print(key, value)

for value in values:
    print(value)

for item in items:
    key = item[0]
    value = item[1]
    print(key, value)


