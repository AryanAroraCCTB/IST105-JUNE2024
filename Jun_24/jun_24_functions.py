# FUNCTIONS

# Syntax
# Declaring/Initialize the function
def function_name ():
    # perform the actions of the function
    print('demo function')

# Calling the function
function_name() 

print('Completed')

# A function can only return 1 thing or nothing at all
# If you wish to return more than 1 value, encapsulate in a single structure
def incrementBy1 (num):
    num += 1
    return num # returning one value

def incrementBy1_2 (num):
    num += 1
    return [num, num, num] # returning more than one value by encapsulation

result = incrementBy1(21) # result = 22
print(f'RESULT: {result}')

# Functions help us reuse code


"""
Function returns the letter grade for the given marks
@params marks
@return grade
""" 
def getGrade(marks):
    if(marks >= 90): # checked
        return 'A'
    elif(marks >= 80): # checked
        return 'B'
    elif(marks >= 70): # checked
        return 'C'
    elif(marks >= 60): # not-checked
        return 'D'
    else: # not-checked
        return 'F'

"""
Function prints the letter grade for the given marks
@params marks
@return 
""" 
def getGrade_2(marks):
    if(marks >= 90): 
        print(f'{marks} is Grade A')
    elif(marks >= 80): 
        print(f'{marks} is Grade B')
    elif(marks >= 70): 
        print(f'{marks} is Grade C')
    elif(marks >= 60): 
        print(f'{marks} is Grade D')
    elif(marks >= 50):
        print(f'{marks} is Grade E')
    else: 
        print(f'{marks} is Grade F')

getGrade_2(77)
getGrade_2(87)
getGrade_2(97)
getGrade_2(57)
getGrade_2(27)

# Exercise :1
# Ques: Write a function that takes in a number num, print if the number is multiple of 2, 3, or 5. If not, print "not a multiple of 2, 3, or 5"
# Hint: modulus % operator
def isMultipleOf(num):
    if num % 2 == 0:
        print(f'{num} Multiple of 2')
    elif num % 3 == 0:
        print(f'{num} Multiple of 3')
    elif num % 5 == 0:
        print(f'{num} Multiple of 5')
    else:
        print(f'{num} Multiple of neither 2, 3 o 5')

isMultipleOf(27)
isMultipleOf(21)
isMultipleOf(25)
isMultipleOf(14)

# Practice Exercise Answers

# q1.  Write a function in python that takes in 3 numbers and returns the sum of all
def sumAll(a,b,c):
    sum = b + c + a
    return sum

def sumAll_2(a,b,c):
    return a + b + c

# q4. 4. Write a function in python that takes in 3 numbers and returns the average of all
def avgAll(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

def avgAll_2(a, b, c):
    return (a + b + c) / 3

def avgAll_3(a, b, c):
    sum = sumAll(a, b, c)
    avg = sum / 3
    return avg

def avgAll_4(a, b, c):
   return sumAll(a, b, c) / 3

# q2. 2. Write a function in python that takes in 3 numbers and returns the max number of all

def maxOfaAll(a, b, c):
    # a: a > b and a > c
    if a > b and a > c:
        return a
    
    # b: b > a and b > c
    if b > a and b > c:
        return b 
    
    # c: c > a and c > b
    if c > a and c > b:
        return c
    
def maxOfaAll_2(a, b, c):
    if a > b and a > c:
        return a
    elif  b > a and b > c:
        return b 
    elif c > a and c > b:
        return c
    else:
        return None

def maxOfaAll_3(a, b, c):
    if a >= b and a >= c:
        return a
    elif  b >= a and b >= c:
        return b 
    elif c >= a and c >= b:
        return c
    else:
        return None
    
def maxOfaAll_edmar(a, b, c):
    if a >= b:
        return a
    elif b >= c:
        return b
    else:
        return c        
    
maxOfaAll(21, 20 , 19)
maxOfaAll(20, 20 , 19)
maxOfaAll(20, 20 , 19)
maxOfaAll(20, 20 , 19)

maxOfaAll(20, 20 , 19)
maxOfaAll(20, 20 , 19)
maxOfaAll(20, 20 , 19)
maxOfaAll(20, 20 , 19)

maxOfaAll_edmar(23, 21, 30) # edge case # QA 
