# While Loops

# Syntax
# val = 0
# while True:
#     print(f'I am looping: {val}')
#     val += 1

# Main Components
val = 0 # start condition
while val <= 5: # end condition
    print(f'I am looping: {val}')
    val += 1 # increment rule

print("Completed")

basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0 # start condition
length = len(basket_of_fruits) - 1 # 25
while index <= length: # 0, 1, 2....25
    fruit = basket_of_fruits[index] # basket_of_fruits[0], basket_of_fruits[1]
    print(f'Index {index} has fruit {fruit}')
    index += 1 # increment rule

index = 0
while index < 5:
    index += 1

list = ['one', 'two', 'three'] # 3 items
[ 0, 1, 2]
list[0] # 'one'
list[1] # 'two'
list[2] # 'three'

# temp = 2
# list[temp] # list[2] -> 'three'
# temp = 3
# list[temp] # list[3] -> ERROR
# temp = 0
# list[temp] # list[0] -> 'one'


# Q. Print all fruits in reverse order using the while loop
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

# Reversing the loop
val = 5 # start condition
while val >= 0: # end condition
    print(f'I am looping: {val}')
    val -= 1 # decrement rule

val = len(basket_of_fruits) - 1 # start condition
while val >= 0: # end condition
    fruit = basket_of_fruits[val]
    print(f'I am looping: {val}, Fruit {fruit}')
    val -= 1 # decrement rule


