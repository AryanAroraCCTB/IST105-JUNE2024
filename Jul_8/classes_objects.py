# Object Oriented Programming(OOPS)

# Class: is higher a level categorization
x = 6 # class int
y = 0 # class int
z = 5 # class int
a = 5 # class int

a = 2.1 # class float
b = True # class boolean
c = ['a', 'b'] # class list

# print(type(x))

# Object: is an instance of a class(higher level category)
x = 6 # object belonging to class int
y = 0 # object belonging to class int
z = 5 # object belonging to class int

# x is different from y
# x is different from z

a = 2.1 # object belonging to class float
b = True # object belonging to class boolean
c = ['a', 'b'] # object belonging to class list
d = ['a', 'c'] # object belonging to class list


# Syntax to Create Class
class Person_:
    first_name = 'JOHN' # class property & their default values
    last_name = 'SMITH' # class property & their default values
    age = 0

x = int(10) # x is an object of class int
print(type(x))

# Syntax to Create Object
y = Person_() # y is an object of class Person
print(type(y))
z = Person_()
a = Person_()
b = Person_()

# Access properties of an Object
print(y.first_name, y.last_name)

my_first_name = y.first_name # JOHN
my_last_name = y.last_name # SMITH

# Modify the properties of an Object
y.first_name = 'JOHN_NEW'
print(y.first_name, y.last_name)

a = Person_()
a.first_name = 'A1'
a.last_name = 'A2'
print(a.first_name, a.last_name)

# New Person Class
class Person_1:
    first_name = '' # properties
    last_name = '' # properties

    # methods
    def greetings(self): # self if the object/instance that called the function/method
        print(f'Hi, My Name is {self.first_name} {self.last_name}')

a = Person_1()
a.first_name = 'JOHN'
a.last_name = 'SMITH'
a.greetings() # a is caller of the greetings method, so self in greetings method refers to a
a.greetings() # a is caller of the greetings method, so self in greetings method refers to a
a.greetings() # a is caller of the greetings method, so self in greetings method refers to a

x = list([1,2,3]) # list class
x.sort() # sort if method of the list class

b = Person_1()
b.first_name = 'MIKE'
# b.last_name = ''
b.greetings()

# Another person class
print('---------------------------------')
class Person_2:
    first_name = '' # properties
    last_name = '' # properties
    bank_balance = 0
    age = 20

    # methods
    def greetings(self): # self if the object/instance that called the function/method
        print(f'Hi, My Name is {self.first_name} {self.last_name}')

    def initials(self):
        print(f'{self.first_name[0]}{self.last_name[0]}')

    def incrementBalance(self, amount):
        self.bank_balance += amount

    def decrementBalance(self, amount):
        self.bank_balance -= amount

a = Person_2()
a.first_name = 'JOHN'
a.last_name = 'SMITH'
a.bank_balance = 100000
a.incrementBalance(100)
a.decrementBalance(10)
a.initials()

b = Person_2()
b.first_name = 'MIKE'
b.last_name = 'TYSON'
b.incrementBalance(10000)
b.incrementBalance(10000000)
b.decrementBalance(100)

# Initializer / Contructor Function
print('---------------------------------')
class Person:
    # Initializer
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.__bank_balance = 0
        self.__year_of_birth = 2024 - age

    # methods
    def greetings(self): # self if the object/instance that called the function/method
        print(f'Hi, My Name is {self.first_name} {self.last_name}')

    def initials(self):
        print(f'{self.first_name[0]}{self.last_name[0]}')

    def viewBalance(self):
        print(f'My Balance is {self.__bank_balance}')
        return self.__bank_balance

    def incrementBalance(self, amount):
        self.__bank_balance += amount

    def decrementBalance(self, amount):
        self.__bank_balance -= amount

a = Person('JOHN', 'SMITH', 20)
a.greetings()
a.initials()
a.incrementBalance(1000)
a.decrementBalance(100)

b = Person(12, 'SMITH', 22)
b.incrementBalance(100)
b.decrementBalance(20)
balance = b.viewBalance()

# Circle Class
print('\n---------------------------------\n')
class Circle:
    def __init__(self, radius, color):
        # private properties
        self.__radius = radius
        self.__color = color
    
    # Getter Methods
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color

    # Setter Methods
    def setRadius(self, radius):
        self.__radius = radius
        return True

    def setColor(self, color):
        self.__color = color
        return True

c1 = Circle(10, 'GREEN')
print(c1.getRadius(), c1.getColor())
print(c1.setRadius(21), c1.setColor('BLUE'))
print(c1.getRadius(), c1.getColor())