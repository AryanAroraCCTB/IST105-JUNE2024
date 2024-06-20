# Variable Name
A = 10
a = 10

_sum = 10

a1 = 10
a = 'c'

# a-z
# A-Z
# 0-9
# _
a_1 = 2

# def = 10
# class = 123

sumOfGrades = 100

# This is sum of all the grades
x = 100

sumOfGrades = 10
SumOfGrades = 10
sum_of_grades = 10

PI = 3.14

# Multiple Values to Multiple Variables
a = 10
b = 11
c = 12

a, b, c = 10, 11, 12
a = b = c = 10
# print(a,b,c)

# List is same as Array
fruits = 'apple', 'orange', 'grapes'
# print(fruits)
# print(type(fruits))

fruits = ['apple', 'orange', 'grapes'] # range is from 0 to 2: 0, 1, 2
# print(fruits)
# print(type(fruits))

# () called a tuple
# [] called a list

# Indexing in a List
# Zero based indexing, meaning counting starts at 0
# One based indexing, meaning counting starts at 1
# print('0th fruit is: ', fruits[0]) # apple
# print('1st fruit is: ', fruits[1]) # orange
# print('2nd fruit is: ', fruits[2]) # grapes
# print('3rd fruit is: ', fruits[3]) # grapes

# x = fruits[0]
# y = fruits[1]
# z = fruits[2]

# Unpacking of values
a, b, c = 10, 11, 12
x, y, z  = fruits
x, y, z  = ['apple', 'orange', 'grapes']
x, y, z  = ('apple', 'orange', 'grapes')
# print(x,y,z)

# Arthmatic Operations
x = 10
y = 5
z = x - y # Add 10 - 5 = 5
z = x + y # Subtract 10 + 5 = 15
z = x * y # Multiply 10 * 5 = 50
z = x / y # Divide 10 / 5 = 2
z = x % y # Modulus 10 % 5 = 0

# 5 * Q + R = 10
# 5 * 2 + 0 = 10

# 10 % 3 = 1
# 10 / 3 = 3
# 3 * Q + R = 10
# 3 * 3 + 1 = 10

# Q. Finding an even number
# x % 2 = 0 # x is even
# x % 2 != 0 # x is odd

# Truthy Falsey Values
# Truthy is simply, 
# - when the statement is correct
# - when there is a value
# Falsey is simply, 
# - when the statement is incorrect
# - where is no value

# Equal operator
x = (3 == 2)
x = False

# Not Equal operator
x = (3 != 2)
x = True
# print(x)
# x = False

x = ((3+2) == (10/2)) # => 5 == 5 -> True
# print(x)

# Greater & Less than Operator
x = (5 >= 3) # True
y = (6 <= 10) # True
z = (1 + 2) # 3
# print(x, y, z)

x = bool(None)
x = bool(1)
x = bool(0)
x = bool(1-1) # bool(0) = False
# print(x)

x = 3
x = x + 1 # x += 1
x = x + 3 # x += 3
x = x + 5 # x += 5

x = x - 1 # x -= 1
x = x / 3 # x /= 3
x = x * 5 # x *= 5
x = x % 5 # x %= 5

# Increment variable
x = 3
x = x + 1
x += 1
# Decrement variable
x = x - 1
x -= 1
# x++ , x--

# Conditional Logic
if(True):
    print('Answer is True')
else:
    print('Answer is False')

if((3 != 2)): # True
    print('3 is not equal to 2')
else:
    print('3 is equal to 2')



grade = 75
if (grade > 67): # 75 > 67 = True
    print('Student passed')
else:
    print('Student failed')

if (grade > 65):
    print('Letter Grade is C')

if (grade > 75): # 75 > 75 = False
    print('Letter Grade is B')

# AND, OR, NOT operator -> RETURN A bool
# AND
# - Is true only if both sides are true
x = True and True # True
x = True and False # False
x = False and True # False
x = False and False # False

x = (5 > 3) and (7 > 5) # True and True = True

# OR
# - Is true if any side says true
x = True or True # True
x = True or False # True
x = False or True # True
x = False or False # False

x = (5 > 3) or (7 > 5) # True or True = True

# NOT
# - Converts true to false & false to true
x = not True # False
x = not False # True

x = not 3 # not True = False
x = not None # not False = True