# Print all items of the list
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

# For LOOP
for fruit in basket_of_fruits:
    print(f'Fruit is {fruit}')

# While Loop
index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]
    print(f'Fruit is {fruit}')
    index += 1

# Print all characters of the string
text = 'This is a very very long text that teaches python3 to students of CCTB.'

# For LOOP
for character in text:
    print(f'Character {character}')

# While Loop
index = 0 
while index < len(text):
    character = text[index]
    print(f'Character {character}')
    index += 1

# Q1. Print index of character 'a' in the text
print('\nQ1. Print index of character \'a\' in the text\n')
text = 'This is a very very long text that teaches python3 to students of CCTB.'
index = 0 
while index < len(text):
    character = text[index]
    
    if character == 'a':
        print(f'Character {character} @ {index}')
    
    index += 1

# Q2. Count the number of times 'a' appears in the text
print('\nQ2. Count the number of times \'a\' appears in the text\n')
text = 'This is a very very long text that teaches python3 to students of CCTB.'
index = 0 
count = 0
while index < len(text):
    character = text[index]
    
    if character == 'a':
        count += 1
    
    index += 1
print(f'a appears {count} times')

# Q3. Print fruits that start with letter g
print('\nQ3. Print fruits that start with letter g\n')
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    if fruit[0] == 'g':
        print(f'Fruit is {fruit}')
        
    index += 1

# Q4. Print fruits that end with letter t
print('\nQ4. Print fruits that end with letter t\n')
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    last_index = len(fruit) - 1 
    if fruit[last_index] == 't':
        print(f'Fruit is {fruit}')
        
    index += 1

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    if fruit[-1] == 't':
        print(f'Fruit is {fruit}')
        
    index += 1

# Q5. Print fruits that have more than 5 letters but less than 7
print('\nQ5. Print fruits that have more than 5 letters but less than 7\n')
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    num_letters = len(fruit)

    if num_letters > 5 and num_letters < 7:
        print(f'Fruit is {fruit}')
        
    index += 1

# Q6. Print fruits that have a letter 'a' in them
print('\nQ6. Print fruits that have a letter \'a\' in them\n')
basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    if 'a' in fruit:
        print(f'Fruit is {fruit}')
        
    index += 1

# Q7. Print the number of worlds in text
print(f'\nQ7. Print the number of worlds in text\n')
text = 'This is a very very long text that teaches python3 to students of CCTB.'

words = text.split(' ')
print(words)
print(len(words))

# Q8. Print fruits that letter a, occurring 2 times
print(f'\nQ8. Print fruits that letter a, occurring 2 times\n')

basket_of_fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'eggplant', 'fig', 'grapefruit', 'huckleberry', 'indian-plum', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectare', 'orange', 'pineapple', 'quinne', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla-fruit', 'watermelon', 'xylia-fruit', 'yumberry/yuzu', 'zuchini']

index = 0
while index < len(basket_of_fruits):
    fruit = basket_of_fruits[index]

    count_of_letter = fruit.count('a')
    if count_of_letter == 2:
        print(f'Fruit is {fruit} with 2 a')
    
    if count_of_letter > 2:
        print(f'Fruit is {fruit} with more than 2 a')
        
    index += 1

# -----------------------
# More Practice Exercises
# -----------------------

# 1. **Print the length of each fruit name.**

# 2. **Count the number of fruits with more than 5 letters.**

# 3. **Print fruits containing the letter 'e'.**

# 4. **Count the number of times 'e' appears in the text.**

# 5. **Print the index of the word 'python' in the text.**

# 6. **Count the number of words in the text.**

# 7. **Print fruits that have 'berry' in their name.**

# 8. **Print fruits that start with a vowel.**

# 9. **Count how many times the substring 'very' appears in the text.**

# 10. **Print fruits that contain exactly 6 letters.**

# 11. **Print the index of the last occurrence of 't' in the text.**

# 12. **Print fruits that contain the letter 'o' but do not end with 'o'.**

# 13. **Count the number of uppercase letters in the text.**

# 14. **Print the fruits in reverse order.**

# 15. **Print the index and value of fruits that start with a consonant.**

# 16. **Count the number of fruits that have a hyphen ('-') in their name.**

# 17. **Print the fruits that have an odd number of letters.**

# 18. **Print the words in the text that are longer than 4 characters.**

# 19. **Count the number of sentences in the text (considering sentences end with a period).**

# 20. **Print the fruits that contain the letter 'a' at least twice.**

# 21. **Print the index of each vowel in the text.**

# 22. **Count the number of unique characters in the text.**

# 23. **Print fruits that have the same first and last letter.**

# 24. **Print the longest word in the text.**

# 25. **Count the number of digits in the text.**

# 26. **Print fruits that have exactly two 'n's in their name.**