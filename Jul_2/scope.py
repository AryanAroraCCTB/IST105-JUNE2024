# Scoping

# Example #1
# Global Scope
a = 3 # global variable

# Local Scope
def sumNumbers(num_1, num_2):
    a = 7 # local variable
    print(f'Local a: {a}')
    sumNum = num_1 + num_2 # local variable
    return sumNum


sumNumbers(1,2)

print(f'Global a: {a}') # 3 or 7 -> answer is 3 since local variable is new

# print(sumNum)

# Example #2
b = 10 # global variable

def sayHi():
    b = 6
    print(f'Hello')

sayHi()

b = 11
print(b)

# Connecting local to global variables
b = 10 # global variable

def sayHiAgain():
    global b
    b = 6
    print(f'Hello')

print(b) # 10
sayHiAgain()
print(b) # 6


# Fun Question
a = 10

def func_1():
    a = 7
    print(f'{a}')
    print(f'I am Func_1')

    def func_2():
        print(f'I am Func_2')

    func_2()
    
    
func_1()

print(a)



a = 10

def func_1():
    global a
    a = 7
    print(f'{a}')
    print(f'I am Func_1')

    def func_2():
        global a 
        a = 11
        print(f'I am Func_2')

    func_2()

    a = 15
    
    
func_1()

print(a) # 15