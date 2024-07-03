# Functions with more than one return value

def sumOfTwo(a, b):
    return a + b # function returning a value

def sumOfTwoAgain(a, b):
    print(f'{a+b}') # function returning no value

# A function can return max of only 1 value, & min of no value

x = 10
y = [1,2,3,4,5,6]

def nearestHigherGrade(grades):
    # lots of work
    return grades


# Before: when you knew that a function can only return a single thing or nothing at all
numbers = [3,7,2,1,2,9]

def maxOfValues(values: list) -> int:
    values.sort()
    return values[-1]

def minOfValues(values):
    values.sort()
    return values[0]

# After: when you now know there is a workaround to return more than a single value
def minMaxTuple(values: list) -> tuple:
    values.sort()
    return (values[0], values[-1])
    

