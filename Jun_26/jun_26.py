# Loops
# A way to repeat code based on a condition


# For Loop: for iteration
# For-in loop
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']
for fruit in basket_of_fruits:
    print(fruit)

x = range(10) # [0,1,2,3...9]
# for y in x: 
#     print(y)

# for value in range(10): # [0,1,2...9]
#     print(f'Value is {value}')


fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']
fruit = fruits[0]
fruit = fruits[1]
fruit = fruits[2]
fruit = fruits[3]




number_of_fruits = len(basket_of_fruits)
print(number_of_fruits)
range_of_fruits = range(number_of_fruits)
print(range_of_fruits) # [0,1,2,3...25] #index

# 0 1 2 3 4 5 6 7 8 9 : counting as computers
# 1 2 3 4 5 6 7 8 9 10 : counting as humans

for index in range_of_fruits:
    print(basket_of_fruits[index]) # printing a value at an index(position)


print('\n-----------------------------\n')

# Range with steps
steps_3 = range(0, 20, 1)
steps_3 = range(0, 20, 2)
steps_3 = range(0, 20, 3)
steps_3 = range(20, 0, 1)
steps_3 = range(0, -20, -3)
steps_3 = range(0, -20, -2)
steps_3 = range(0, -20, -1)
for val in steps_3:
    print(val)
    