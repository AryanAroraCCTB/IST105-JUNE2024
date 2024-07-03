# Participation Exercise #5

# 1. Write a loop to print numbers from 0 until 100
numbers = range(0, 101)
for val in numbers:
    print(val)

index = 0
while index <= 100:
    print(index)
    index += 1

# 2. Write a loop to print odd numbers from 0 until 100 
for val in range(1, 101, 2):
    print(val)

for val in range(0, 101):
    # allow to print only odd values
    if val % 2 != 0:
        print(val)

index = 1
while index <= 100:
    print(index)
    index += 2

# 3. Write a loop to print even numbers from 0 until 100
for val in range(2, 101, 2):
    print(val)

for val in range(0, 101):
    # allow to print only even values
    if val % 2 == 0:
        print(val)  

index = 2
while index <= 100:
    print(index)
    index += 2

# 4. Make a list of countries(a-z), print all one by one using a loop

# 5. 0 - 100, IF ODD: val is odd, IF EVEN: val is even
for val in range(0, 101):
    if val % 2 == 0:
        print(f'{val} is even')
    
    if val % 2 != 0:
        print(f'{val} is odd')