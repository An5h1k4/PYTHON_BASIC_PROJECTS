# name = "James"
# print(isinstance(name, str))
# print(type(name) == str) 
# age = 2
# print(isinstance(age, int))
# frenzi = "Confused"
####Type Conversion 
number = "20"
age = int(number)
print(type(age))
print(type(number))

# complex for complex numbers
# bool 
# list for lists
# tuples for tuples
# range fot range
# dict for dicttionaries
# set for sets


x=  4/3
z= 4//3
print(x)
print(z)



# ternary operator
print("ternary operator")
def isadult(age):
    if age > 18:
        return True
    else:
        return False

def isadult2(age):
    return True if age>18 else False

verdict = isadult(22)
verdict2 = isadult2(2)
print("Verdict 1 {22}: "+ str(verdict))
print("Verdict 2 {2}: " + str(verdict2))

print(""" Anshika is 
      19 years old
      and she is beautiful""".upper())
print(""" Anshika is 
      19 years old
      and she is beautiful""".lower())
print(""" Anshika is 
      19 years old
      and she is beautiful""".title())
print(""" Anshika is 
      19 years old
      and she is beautiful""".islower())


# COMMON ONES
# isalpha() if str has only chars and is not empty
# isnum() if str has only chars or digits and is not empty
# isdecimal() if str has digits is not empty
# startswith() if str has only chars and is not empty
# isalpha() if str has only chars and is not empty
# all these will create a new modified string and do not alter the original string
# check whatsapp 
name = "Anshika"
print(name.lower())
print(name)
print(len(name))
print("ka" in name)
char = "Anshika \"The Goddess\""
print(char)
print(name[1])
print(name[1:3])
print(name[:3])
done = True
done = 0 
done = "" # list tuple and dictionaries are only false when they are empty
if done:
    print("yes")
else:
    print("Not yet")
dac = 10
print(type(dac) == bool)
complexNum = 10 + 3j
num = complex(2,3)
print(complexNum)
print(num)
print(num.real,num.imag)
print(round(-5.5))
print(round(5.5))
print(round(5.49,1))


# Enumeration
# from enum import Enum
# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1
# print(list(State))
# print(len(State))
# yourage = input("What is your age? ")
# print("Your age is: "+ yourage)



# Lists
dogs = ["Roger", "Octavia", "Boe", 12]
# print("Aiu" in dogs)
dogs[3] = "Aiu"
print("Aiu" in dogs)
print(dogs[0:4])
dogs.append("Joe")
print(dogs)
dogs.extend(["Jule",5])
dogs += ["Dextor"] 
print(dogs)
dogs.remove(5)
print(dogs)
print(dogs.pop())
dogs.insert(2,"inserted")
dogs[1:1] = ["space1","space2"]
print(dogs)
dogs.sort(key = str.lower) #since the regular sorting function sorts the capital letters strings alphabetically then the small ones we use key = str.lower() to ignore the capital letters or small letter and sort them ordinarily
dogsCoppy = dogs[:]
print(dogsCoppy)
# we can create a new list without modifying the original list by creating a global function named sorted insted items.sort()
# print(sorted(item, key = str.lower))           sorted function takes the list and the way to sort the data as its perameters




# Tuples
# make immutable onjects
names = ("Dodger", "Octavia", "James", "Jules", "Alpine", "Buxy")
names[-1]
names.index("Dodger")
len(names)
print("Dodger" in names)
names[0:2]
# in sorted function for tuple it will create a new tuple
print(sorted(names))
print(names) #does not modify the original tuple
newTuple = names + ("Anshika", "Brian", "Bucky")
print(newTuple)


# dictionaries
dog = {"name": "Roger", "age" : 8, "breed": "Golden retriver", "color":"pink"}
# dog["name"] = "Syd"
print(dog.get("color", "blond"))
print(dog["name"])
print(dog.pop("name"))
print(dog)
print(dog.popitem())
print(dog)
print("color" in dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
dog["Favorit food"] = "Meat"
del dog['color']
dogCopy = dog.copy()
print(len(dog))



# Sets
names = {"Roger", "Sydni", "Sammy"}
names2 = {"Roger", "Micky", "Duna"}
intersect = names2 & names2
print(intersect)
union = names | names2
print(union)
union = names > names2
print(union)
union = names < names2
print(union)




# Functions 
def hello(name = "traveler", age = 10):
    print("Hello "+ name+" you must be "+ str(age) + " years old")

hello("Steve",106)
hello("Anshika",20)
hello("Bucky",107)
# hello()
def hello(name):
    # if not name:
    #     return 
    print("Hello "+ name+"!")
    return name, "Winchester", 8
hello("Boey")
print(hello("Anshika"))

def test():
    age = 8
    print(age)
print(age)
test()

def counter():
    count = 0
    def increment():
        nonlocal count 
        count += 1
        return count
    return increment

increment = counter()
print(increment())
print(increment())
print(increment())


Objects
everything in python is objects
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())

items = [1,2,3]
items.append(3)
items.pop()
print(id(items)) #tells the location of the memory


# Loops 
# count = 0
# while count < 10:
#     print("The count is: "+ str(count))
#     count+=1
# print("Now yore outside the loop")
items = ["Lui", "Anshika", "James", "Henry"]
for index , items in enumerate(items):
    print(index,items)



# classes and inheritance
class Animal:
    def Walk(self):
        print("Hay!.. I'm walkin 'nere..")
class Dog(Animal): #inheriting Animal class 
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
        print("This is inside the constructor with \nName: "+name+"\nAge: "+str(age))
    def bark(self):
        print("Woof! woof! XD")
roger = Dog("Roger", 8)
octavia = Dog("octavia", 9)
print(roger.name)
print(roger.age)
roger.bark()
roger.Walk()


# Modules
# import Modules 
# Modules.bark()
from CustLib.Modules import bark
bark()

# Accptaing Arguments
# import sys
# print(sys.argv)
import argparse
parser = argparse.ArgumentParser(
    description = "This program prints the name of my dogs"
)
parser.add_argument('-c', '--color',metavar='color', required = True,   choices={'red', 'yellow'}, help = 'the color to search for' )
args = parser.parse_args()
print(args.color)



# lambda function
lambda num : num * 2 
exponent = lambda a,b : a **b

print(exponent(2,3))



# map( ), filter(), reduce()
# number = [1,2,3,4]
# def double(a):
#     return a * 2
# #  [doing it as a lambda function would be] double = lambda a : a * 2
# result = map(double, number)  # can also be written as and remove the function definatinon  result = map(lambda a: a*2, number)
# print(list(result))


# numbers = [1,2,3,4,5,6,7,8,9,10]
# def isEven(n):
#     return n % 2 == 0
# # or can be written as result = filter(lanbda n : n % 2 == 0, numbers)

# result = filter(isEven, numbers)
# print(list(result))

from functools import reduce
expenses = [('dinner',80), ('car repair',120)]
sum = reduce(lambda a,b: a[1] + b[1], expenses)
print(sum)

# Recursion
def function(n):
    if n == 1: 
        # print("X 1")
        return 1
    # print("X "+ str(n))
    return n * function(n - 1)

print(function(7))



# decorators
def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello")

hello()



# docstrings
def increment(n):
    """Incrementing a number"""  #<---- docstrings
    return n + 1
class Dog:
    """A class representing a dog and its trates"""
    def __init__(self, name,age,breed):
        "A constructor to initialize a new dog "
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark():
        """A function that makes the dog bark"""
        print("Wof! Wof!")
    def walk():
        """A function that makes the dog walk"""
        print("Walking...")
class Cat:
    """A class representing a cat and its trates"""
    def __init__(self, name,age,breed):
        "A constructor to initialize a new cat "
        self.name = name
        self.age = age
        self.breed = breed
    
    def purr():
        """A function that makes the cat bark"""
        print("purrrrr....rrrr")
    def walk():
        """A function that makes the cat walk"""
        print("Walking...")
print(help(Dog))
print(help(Cat))


# Annotations 
def increment(n):  #A fuction without annotation
    return n+1
def decremetn(n : int) -> int:
    return n -1;

count: int = 10



# Exception Handeling
# try:
#     result = 2 /0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     result = 1;
# print(result)
# try:
#     raise Exception("An error")
# except Exception as error:
#     print(error)

# class DogNotFoundException(Exception):
#     print("inside dog not found")
#     pass

# try:
#     raise DogNotFoundException()
# except DogNotFoundException:
#     print("Dog is not found")
# fileName = '/c/Data Science/PYTHON_BASIC_PROJECTS/test.txt'
# try:
#     file = open(fileName,'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()
fileName = 'c/Data Science/PYTHON_BASIC_PROJECTS/test.txt'
with open(fileName, 'r') as file:
    content = file.read()
    print(content)


# pip   to install third party packages


#######################################################
number = [1,2,3,4,5,6,7,8]                           #
numbers_power2 = [n**2 for n in number]              #  
print(numbers_power2)                                #  
numbers_power2 = []                                  #  
for n in number:                                     #  
    numbers_power2.append(n ** 2)                    #  
numbers_power2 = list(map(lambda n : n **2, number)) # 
#######################################################




# Polymorhysim
class Dog:
    def eat(self):
        print("Eating dog food! yum yum yum")
    
class Cat:
    def eat(slef):
        print("Eating Cat food! yum yum yum")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()



# Operator Overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is the constructor of the dog class")
    def __gt__(self, other):
        return True if self.age > other.age else False
roger = Dog('Roger', 8)
Octavia= Dog('Ocatvia', 7)

print(roger > Octavia)
# __add__, __lshift__ and so on

