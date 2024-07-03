# Strings

name = 'JOHN'
print(type(name))
print(name)

numbers = [1,2,3]
element = numbers[0] # 1
element = numbers[1] # 2
element = numbers[2] # 3
numbers[2] = 4 # [1,2,4]

# Getting character of a string
name = 'JOHN'
character = name[0] # J
print(character)
character = name[1] # O
print(character)
character = name[2] # H
print(character)
character = name[3] # N
print(character)

print('-------')

index = 0
while index < len(name):
    print(name[index])
    index += 1

print('-------')

for character in name:
    print(character)

# Conditionals of strings
text = 'This is a very long text'
target_string = 'This'

if target_string in text:
    print('Found this')

if target_string not in text:
    print('Not Found this')

print('-------')

# Subset of a string
element = name[0:2]
print(element)
element = name[0:]
print(element)
element = name[1:3]
print(element)

# Helper functions
name = 'john'

print('-------')

name = name.upper() # JOHN
print(name)

name = name.lower() # john
print(name)


# Split Function
students = 'a,b,c,d,e,f,g,h,i'

print('-------')

students_list = students.split(',')
print(students_list)

students = 'a | b | c | d | e | f | g | h | i'

print('-------')

students_list = students.split(' | ')
print(students_list)

# Concatenate strings i.e. Adding strings together
first_name = 'JOHN'
last_name = 'SMITH'

print('-------')

full_name = first_name + ' ' + last_name
print(full_name)

full_name = f'{first_name} {last_name}'
print(full_name)