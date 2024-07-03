# IF-ELSE
# Syntax
age = 20
if(age >= 21):
    print('age is larger than 21')
else:
    print('age is lesser than 21')

age = 26
if (age >= 25):
    print('25+')

if (age >= 21 and age < 25):
    print('21+')


# IF-ELIF-ELSE
age = 26
if (age >= 25):
    print('25+')
elif (age >= 21):
    print('21+')
else:
    print('20-')

print('completed')

marks = 77
# Grading Strategy
# 90-100 : A
# 80-89 : B
# 70-79 : C
# 60-69 : D
# 0-59 : F

# if-else strategy
if (marks >= 90 and marks <= 100): # checked
    print('A')

if (marks >= 80 and marks <= 89): # checked
    print('B')

if (marks >= 70 and marks <= 79): # checked
    print('C') 

if (marks >= 60 and marks <= 69): # checked
    print('D')

if (marks < 60): # checked
    print('F')

# if-elif-else strategy
if(marks >= 90): # checked
    print('A')
elif(marks >= 80): # checked
    print('B')
elif(marks >= 70): # checked
    print('C')
elif(marks >= 60): # not-checked
    print('D')
else: # not-checked
    print('F')

print('completed')

# Note: if-elif-else is faster and more efficient than if-else blocks


# Exercise :1
# Ques: Given a number num, print if the number is multiple of 2, 3, or 5. If not, print "not a multiple of 2, 3, or 5"
# Hint: modulus % operator
num = 6

# print atleast one multiple
if num % 2 == 0:
    print(f'{num} Multiple of 2')
elif num % 3 == 0:
    print(f'{num} Multiple of 3')
elif num % 5 == 0:
    print(f'{num} Multiple of 5')
else:
    print(f'{num} Multiple of neither 2, 3 o 5')

# print all that are the multiples
if num % 2 == 0:
    print(f'{num} is Multiple of 2')

if num % 3 == 0:
    print(f'{num} is Multiple of 3')

if num % 5 == 0:
    print(f'{num} is Multiple of 5')

if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print(f'{num} is Multiple of neither 2, 3 o 5')


# Print Functions
print("Hi")

a = 12
b = a + 1
print(a)

print('This number is:', a, ' Increment this: ', b)

name = 'STUDENT_NAME'
age = 25
id = 'CCTB1234567890'

print('My name is', name, 'My age is', age, 'My student id', id)
print(f'My name is {name} My age is {age} My student id {id}') # f-string

print(f'THIS IS LINE 1 \nTHIS IS LINE 2') # \n : new line





































# RANDOMS(import random)
# STRING Functions
