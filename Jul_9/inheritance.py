# SHAPE -> Main Category -> Parent Class
# RECTANGLE, CIRCLE, TRIANGLE, SQUARE -> Sub Categories -> Child Class

# --

# SHAPE (Parent Class) has properties [color, border-width]

# RECTANGLE  (Child Class) inherits properties such as [color, border-width] + have their own properites as well such as [Length + Width]
# CIRCLE (Child Class) inherits properties such as [color, border-width] + have their own properites as well such as [Radius]
# TRIANGLE (Child Class) inherits properties such as [color, border-width] + have their own properites as well such as [Side1 + Side2 + Side3]
# SQUARE (Child Class) inherits properties such as [color, border-width] + have their own properites as well such as [Side]

# --

# SHAPE will have [color, border-width]

# RECTANGLE inherit [color, border-width] + their own [Length + Width]
# CIRCLE inherit [color, border-width] + their own [Radius]
# TRIANGLE inherit [color, border-width] + their own [Side1 + Side2 + Side3]
# SQUARE inherit [color, border-width] + their own [Side]

# --

# Implementation
class Shape:
    def __init__(self, color, border_width) -> None:
        # add error handling here
        self.__color = color
        self.__border_width = border_width

    # Getters
    def getColor(self): return self.__color
    def getBorderWidth(self): return self.__border_width

    # Setters
    def setColor(self, color): self.__color = color
    def setBorderWidth(self, border_width): self.__border_width = border_width

class Rectangle(Shape):
    def __init__(self, length, width, color, border_width) -> None:
        # Shape.__init__(self, color, border_width)
        super().__init__(color, border_width)
        self.__length = length
        self.__width = width
    
    # Getters
    def getLength(self): return self.__length
    def getWidth(self): return self.__width

    # Setters
    def setLength(self, length): self.__length = length
    def setWidth(self, width): self.__width = width

    # Helper Methods
    def calculatePerimeter(self): return 2 * ( self.__length +  self.__width ) # 2 * (l + w)
    def calculateArea(self): return self.__length * self.__width

# s1 = Shape('blue', 10)
r1 = Rectangle(11, 7, 'gold', 3)

print(r1.getLength(), r1.getWidth())
print(r1.getColor(), r1.getBorderWidth())

# -- Sub Childs

# SHAPE will have [color, border-width]
# RECTANGLE(SHAPE) inherit [color, border-width] + their own [Length + Width]
# ABSTRACT_SHAPE(RECTANGLE) inherit [color, border-width, Length, Width] + their own [radius]

# Example #2
class Person:
    def __init__(self, fname, lname, age) -> None:
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    # Getters
    def getFname(self): return self.__fname
    def getLname(self): return self.__lname
    def getAge(self): return self.__age

    # Setters
    def setFname(self, fname): self.__fname = fname
    def setLname(self, lname): self.__lname = lname
    def setAge(self, age): self.__age = age

class Student(Person):
    def __init__(self, fname, lname, age, id, schoolName) -> None:
        super().__init__(fname, lname, age)
        self.__id = id
        self.__schoolName = schoolName 

    # Getters
    def getId(self): return self.__id
    def getSchoolName(self): return self.__schoolName

    # Setters
    def setId(self, id): self.__id = id
    def setSchoolName(self, schoolName): self.__schoolName = schoolName

s1 = Student('s1', 's2', 20, 1234567890, 'CCTB')

class Worker(Person):
    def __init__(self, fname, lname, age, id, officeName) -> None:
        super().__init__(fname, lname, age)
        self.__id = id
        self.__officeName = officeName 
    
    # Getters
    def getId(self): return self.__id
    def getOfficeName(self): return self.__officeName

    # Setters
    def setId(self, id): self.__id = id
    def setOfficeName(self, officeName): self.__officeName = officeName

# Person(parent class): a person can be student or worker or neither
# - Student(child class): every Student is a Person
# - Worker(child class): every Worker is a Person

# s1 = Student()
# w1 = Worker()
# p1 = Person()


# Exercise
# Inheritance
# You have to create a parent class(Animal)
# Then create 3 Child Classes

# Polymorphism
class Animal:
    def __init__(self, legs) -> None:
        self.__num_legs = legs

    def greetings(self):
        print(f'I am an animal')

class Dog(Animal):
    def __init__(self, legs) -> None:
        super().__init__(legs)

    def greetings(self):
        print(f'I am a dog')

class Cat(Animal):
    def __init__(self, legs) -> None:
        super().__init__(legs)
    
    def greetings(self):
        print(f'I am a cat')

class Frog(Animal):
    def __init__(self, legs) -> None:
        super().__init__(legs)

    # def greetings(self):
    #     print(f'I am a frog')

d1 = Dog(4)
d1.greetings()

c1 = Cat(4)
c1.greetings()

f1 = Frog(4)
f1.greetings()

# Exercise
# Parent(SHAPE class)
# Create 4 child classes RECTANGLE, CIRCLE, SQUARE & TRIANGLE
# Using polymorphism implement the calculatePerimeter & calculcateArea Function