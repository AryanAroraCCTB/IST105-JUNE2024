# Lists
# Similar to arrays in js

basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']
basket_of_fruits_2 = ['apple', 'banana', 'cherry']

# Zero based indexing: counting starts at 0

# Access Elements of a list
print(f'{basket_of_fruits[0]}')
print(f'{basket_of_fruits[1]}')
print(f'{basket_of_fruits[2]}')

fruit = basket_of_fruits[0]

# Modifying the element of a list at an index
fruit = 'appricot'
basket_of_fruits[0] = 'appricot'

print(f'-------')
print(f'{basket_of_fruits[0]}')
print(f'{basket_of_fruits[1]}')
print(f'{basket_of_fruits[2]}')

# Subset of a list
# Syntax: list[start_index:end_index]

fruits = basket_of_fruits[0:3] # 0, 1, 2
fruits = [ basket_of_fruits[0], basket_of_fruits[1], basket_of_fruits[2] ]
fruits = basket_of_fruits[0:10] # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(fruits)

# Access elements of a list +ve & -ve
first_fruit = basket_of_fruits[0]

last_index = len(basket_of_fruits) - 1
last_fruit = basket_of_fruits[last_index]

# some_fruit = basket_of_fruits[26] # IndexError: list index out of range

some_fruit = basket_of_fruits[-1]
print(some_fruit)

some_fruit = basket_of_fruits[-5]
print(some_fruit)

# Subsets

fruits = basket_of_fruits[0:9]
fruits = basket_of_fruits[-10:]

fruits = basket_of_fruits[5:len(basket_of_fruits) - 1]
fruits = basket_of_fruits[:9] # defaults start_index = 0
fruits = basket_of_fruits[9:] # defaults end_index to last_index

fruits = basket_of_fruits[15:]
fruits = basket_of_fruits[0:10]
fruits = basket_of_fruits[0:len(basket_of_fruits) - 11]
print(fruits)

# Helper Functions

# Add elements to a list
numbers = [1,2,3]
numbers.append(4) # aka push operation i.e. adding item to the end of the list
print(numbers)


# Remove the element from the list
numbers.pop() # removes the item from the end of the list. Equivalent to numbers.pop(3)
print(numbers)

numbers.pop(0) # index of element to be removed
print(numbers) # [2,3]

numbers.pop(0) # index of element to be removed
print(numbers) # [3]

numbers.clear()
print(numbers)

# Internal logic
# def clear(list):
#     while len(list) > 0:
#         list.pop()

# Problem with referencing
list_a = ['a', 'b', 'c']
list_b = list_a # ['a', 'b', 'c'] shallow copy

list_a.pop() 

print(list_a) # ['a', 'b']
print(list_b) # ['a', 'b', 'c']

# Solution of copy 
list_a = ['a', 'b', 'c']
list_b = list_a.copy() # deep copy

list_a.pop() 

print(list_a) # ['a', 'b']
print(list_b) # ['a', 'b', 'c']

# Count
letters = ['a', 'b', 'a', 'b', 'c']
count_of_a = letters.count('a')
print(count_of_a)

# Index of value
print(letters.index('c'))
print(letters.index('a'))
print(letters.index('a', 1, 3))

# Sort
letters.sort()
print(letters)

# Reverse
letters.reverse()
print(letters)

# Insert
letters.insert(3, 'test')
letters.insert(3, 'test')
print(letters)

# Remove
letters.remove('test')
print(letters)

# Extend
letters.extend([1,2,3])
print(letters)

# Logic of count function
letters = ['a', 'b', 'a', 'b', 'c']

def count(values, str):
    count_of_str = 0
    for val in values:
        if val == str:
            count_of_str += 1
    return count_of_str

print(count(letters, 'a'))