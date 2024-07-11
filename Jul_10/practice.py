
# Practice IST 105

# Lists & Dictionaries
# Q1: 
# Given a list of integers, write a function that returns a dictionary where the keys are the integers and the values are the squares(number * number) of those integers.

def square_dict(numbers) -> dict:
    new_dict = {}
    for number in numbers:
        new_dict[number] = number * number
    return new_dict

result = square_dict([1,2,3,4,5,6]) 
print(result)
# {
#   1: 1, 
#   2: 4, 
#   3: 9, 
#   4: 16, 
#   5: 25, 
#   6: 36
# }

# Q2:
# Write a function that takes two dictionaries and merges them into one. If they have common keys, add their values together. Assume both dictionaries are of equal length

def merge_dict(numbers1: dict, numbers2: dict) -> dict:
    merged_dict = {}
    for item in numbers1.items(): # adds numbers1 to merged_dict
        key = item[0]
        value = item[1]
        merged_dict[key] = value

    keys = merged_dict.keys() # [1,2,3]
    for item in numbers2.items(): # adds numbers2 to merged_dict
        key = item[0]
        value = item[1]
        if key in keys:
            merged_dict[key] = value + merged_dict[key]
        else:
            merged_dict[key] = value
    
    return merged_dict

result = merge_dict({1: 1, 2: 4, 3: 9}, {4: 16, 5: 25, 6: 36}) 
print(result)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

result = merge_dict({1: 1, 2: 4, 3: 9}, {3: 9, 4: 16, 5: 25}) 
print(result)
# {1: 1, 2: 4, 3: 18, 4: 16, 5: 25}


# Tuples
# Q3. Given a tuple of numbers, write a function to return a new tuple with each element squared.

def squared_tuple(numbers: tuple) -> tuple:
    new_numbers = []
    for number in numbers:
        new_numbers.append(number * number)

    return tuple(new_numbers)

result = squared_tuple((1,2,3)) # (1,4,9)
print(result)

# Q4. Write a function that takes a string and returns a tuple containing the string and the length of the string.

def string_length(string: str) -> tuple:
    return (string, len(string))

result = string_length('THIS IS A WORD') # (''THIS IS A WORD', 14)
print(result)

# Sets

# Q5. Write a function that takes two lists and returns the union and intersection of the lists as sets.

def union_intersection_lists(numbers1: list, numbers2: list) -> list:
    num1 = set(numbers1)
    num2 = set(numbers2)
    union = num1.union(num2)
    inter = num1.intersection(num2)
    return [union, inter]

result = union_intersection_lists([1,2,3], [3,4,5]) # [{1,2,3,4,5}, {3}]
print(result)

# Q6. Write a function that takes a list of integers and returns a set of the integers that are greater than a given threshold.

def greater_than_threshold(numbers: list, threshold: int) -> set:
    new_numbers = []
    for number in numbers:
        if number > threshold:
            new_numbers.append(number)
    
    return set(new_numbers)

result = greater_than_threshold([1,2,3,4,5,6,7,8], 3) # {4,5,6,7,8}
print(result)

# Q7. Write a function that takes a list of strings and returns a list of the strings in reverse order. Reverse the string & Reverse the list as well

def reverse_list_string(strings: list) -> list:
    def reverse_word(word: str) -> str:
        reversed_letters = [] 
        for letter in word:
            reversed_letters.append(letter)
        reversed_letters.reverse() # [H, E, L, L, O] -> [O, L, L, E, H] 

        reversed_word = ''.join(reversed_letters) # [O, L, L, E, H] -> OLLEH
        return reversed_word

    new_strings = []
    for word in strings:
        reversed_word = reverse_word(word)
        new_strings.append(reversed_word)

    return new_strings.reverse() # ['OLLEH', 'DLROW'] -> ['DLROW', 'OLLEH']


new_strings = []
def reverse_list_string_2(strings: list) -> list:
    for word in strings:
        reversed_letters = word.split('').reverse() # [H, E, L, L, O] -> [O, L, L, E, H] 
        
        reversed_word = '' # [O, L, L, E, H] -> OLLEH
        for letter in reversed_letters: # [O, L, L, E, H] -> O_L_L_E_H
            reversed_word += letter

        new_strings.append(reversed_word)

    
    return new_strings.reverse() # ['OLLEH', 'DLROW'] -> ['DLROW', 'OLLEH']



result = reverse_list_string(['HELLO', 'WORLD']) # ['DLROW', 'OLLEH']
print(result)

# Q8: Write a function that takes a list of integers and returns a list of the prime numbers in the list.

def list_primes(numbers: list) -> list:
    def is_prime(number: int) -> bool:
        index = 2
        while index < number:
            if number % index == 0: # 17%3 = 0
                return False
            index += 1
        return True

    new_numbers = []
    for number in numbers:
        # decide if prime
        if is_prime(number):
            new_numbers.append(number)

    print(new_numbers)


list_primes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) # [2, 3, 5, 7, 11]
