"""
From
https://learnxinyminutes.com/docs/python/
https://quickref.me/python
"""

"""
Starting Point
"""

# Execute if main program
if __name__ == "__main__":
    pass
    

"""
Print
"""

# Change the end from defaulting to new line
print("hello", end="!")

"""
Arithmetic Operators
"""

# Division is always a decimal

10 / 2        # => 5.0 

# Floor division rounds toward -infinity
5 // 3        # => 1
-5 // 3       # => -2

# Modulo is messy with negatives
-7 % 3        # => 2

"""
Conditional Operators
"""

not True      # => False

True and True # => False
True or False # => False

# Boolean treated as primitive
True + True   # => 2
False -5      # => -5

"""
Comparison Operators
"""

# Equality operator
# Applies bool() to both sides
# but returns the original value
0 and 2       # => 0
-5 or 0       # => -5
2 or True     # 2
True or 2     # True

# True and False are actually 1 and 0
0 == False    # => True
2 > True      # => True
2 == True     # => True

# None, 0, and empty evaluate to False
# All other values are True
bool("")      # => False
bool([])      # => False
bool(4)       # => True
bool(-1)      # => True

# Chaining for checking range / between
1 < 2 < 3     # => True
2 < 3 > 2     # => True

# is vs ==
# is checks by reference
# == checks by value

# None is an object, use is for comparison
"etc" is None  # => False

# Ternary operator
"yay!" if 0 > 1 else "nay!"

"""
Conditionals
"""

if False:
    pass
elif False:
    pass
else:
    print("this will print")

"""
Loops
"""

# For Loop
for animal in ["dog", "cat"]:
    print("{} is a animal").format(animal)
for i, animal in enumerate(["dog", "cat"]):
    print(i, animal) # => 0 dog 1 cat
for name, position in {"Chris": "Programmer", "Enzo": "Therapist"}:
    print(name, "is a", position)
for i in range(4):
    print(i)         # => 0 1 2 3
range(1, 3)          # => 1 2
range(0, 5, 2)       # => 0 2 4

# While Loop
while True:
    print("infinite loop")
    break
    continue

"""
Variables
"""

# Declarations not allowed
a # => Raise NameError

# Naming Convention
# snake_case

# Global scope
x = 5           # global
def my_func():
    global y    # global

"""
Strings
"""
# Multiline
my_str = """multi
line
string"""

# Concat
"Hello" + "world!"
"Hello" "world"

# Index
"hello"[0] # 'H'

# Length
len("This is a string") # => 16

# f-strings (Python 3.6)
name = "chris"
f"{name} is {len(name)} characters long."

"""
List
"""

li = []

# Append/Insert
li.append(5)
li.append(6)
li.insert(2, 8)     #insert(index, value)
li.insert(2, 7)

# Index
li[0]               # => 99
li[-1]              # => 5
li[10]              # Raises an IndexError
li.index(5)         # => 0 # returns index of value

# Slice
# [start:until:step]
li[1:3]             # => [6,7]
li[2:]              # => [7,8]
li[:3]              # => [5,6,7] 
li[::2]             # => [5, 7]
li[::-1]            # => [8,7,6,5] # reverse order

# Pop/Remove
li.pop()            # remove from end
del[2]              # remove by index
li.remove(7)        # remove by value
li.remove(7)        # Raises a ValueError

# Check for existence

1 in li

"""
Tuples
"""

# Immutable list
tup = (1,2,3)

# Length of 1 requires ,
tup = (1,)

# Tuple by default
4,5,6 # => (4,5,6)

# Apply function to each value
list(map(max, [1,2,3], [4,2,1]))           # => [4,2,1]

# Filter out values
list(filter(lambda x: x > 5, [3,4,5,6,7])) # => [6,7]

"""
Dict
"""

# {key: value}
filled_dict = {"one": 1, "two": 2, "three": 3}

# Key must be immutable type
invalid_dict = {[1,2,3]: "123"} # Raises TypeError: unhashable type
valid_dict = {(1,2,3): "123"}

# Get all keys
list(valid_dict.keys())   # Python <3.7 = random order, Python 3.7+ = in order

# Get all values
list(valid_dict.values()) # Python <3.7 = random order, Python 3.7+ = in order

# Check for existing key
"four" in filled_dict      # => False

# Get by key
filled_dict["four"]        # Raises KeyError
filled_dict.get("four")    # => None
filled_dict.get("four", "default")    # => 'default value'

# Set if key not defined
filled_dict.setdefault("four", 4)

# Set key and value
filled_dict["four"] = 4

# Remove key
del filled_dict["four"]

# Dict Comprehension / One line loop
# {*return* *loop* *condition*}
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}

"""
Sets
"""

# Unique tuple
my_set = {1,1,2,3} # => {1,2,3}

# Values have to immutables
invalid_set = {[1], 1}

# Add
my_set.add(4)

# Intersection (overlap)
my_set & {3,4,5}     # => {3,4}

# Union
my_set | {3,4,5}     # => {1,2,3,4,5}

# Difference (only look at left)
my_set - {4,5,6}     # => {1,2,3}

# Symmetric Difference (look at both)
my_set ^ {2,3,4,5,6} # => {1,6}

# Superset (child)
{1,2} >= {1,2,3}    # => False
{1,2} <= {1,2,3}    # => True

# Check if exists
2 in my_set          # => True

# Copy (by value)
my_copy = my_set.copy()
my_copy is my_set     # => False

"""
Functions
"""
def add(x,y):
    return x + y, x, y  # return multiple values as tuple

# Positional Arguments
add(5, 2)

# Keyword Arguments
add(y=5, x=2)
add({"y":5, "x":2})     # the same

# Catch all Positional Arguments
def all_positional(*args):
    return args

# Catch all Keyword Arguments
def all_keyword(**kwargs):
    return kwargs

# Both catch all
def my_func(*args, **kwargs):
    pass

# First class functions
# (functions are treated like variables)
# functions can be passed as an argument, returned, assigned to another variable
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
add_10(3)

# Refer to variables in the parent function
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg

# Use Once functions / Anonymous Functions
(lambda x: x > 2)(3) # => True

"""
Decorators
"""

# Wrappers
def log_function(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@log_function               # equivalent:
def my_function(x,y):       # def my_function(x,y):
    return x+y              #   return x+y
                            # my_function = log_function(my_function)

# Preserve function details of decorated functions
from functools import wraps

def log_function(func):
    @wraps(func) # docstring, function name, arguments list, etc. are copied to the wrapper
    def wrapper(*args, **kwargs):
        print("Entering", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting", func.__name__)
        return result
    return wrapper

@log_function
def my_function(x,y):
    return x+y
my_function(1,2)
my_function.__name__             # => 'my_function'
my_function.__code__.co_argcount # => 2
    
    

"""
Class
"""

class Human:
    species = "H. sapiens"      # class attribute
    
    def __init__(self, name):   # constructor (__ denotes special method)
        self.name = name        # instance attribute
        self._age = 0           # instance attribute (_ denotes to use internally)
        
    def sing(self):             # instance method (self is instance object)
        return "{} sings hallelujah".format(name=self.name)
    
    @classmethod
    def get_species(cls):       # class method (cls is class object)
        return cls.species
    
    @staticmethod               # static method (no class or instance object)
    def grunt():
        return "*grunts*"
    
    @property                   # getter method (trivial getters and setters not required in python)
    def age(self):
        return self._age
    
    @age.setter                 # allows the property to be set
    def age(self, age):
        self._age = age
    
    @age.deleter                # allows property to be deleted
    def age(self):
        del self._age
        
i = Human(name="Ian")
i.say("hi")
Human.species
Human.grunt()
i.grunt()
del i.age

"""
Inheritance
"""

# Allows methods and variables to be inherited from their parent class
class Superhero(Human):
    species = "Superhuman"      # override parents' attributes
    
    def _init_(self, name, superpowers=["super strength", "bulletproofing"]):
        self.fictional = True
        self.superpowers = superpowers
        super().__init__(name)  # inherits age attribute
    
    def sing(self):             # override parents'
        return "dun , dun, dun!"

# Check if instance of
sup = Superhero(name="Spider-Man")
if isinstance(sup, Human):
    print("I am a human")
if type(sup) is Superhero:
    print("I am a superhero")
    
# Get method resolution order
Superhero.__mro__ # <class '__main__.Superhero'>
                  # <class 'human.Human'>

# Call parent method and get local class attribute
sup.get_species() # => 'Superhuman'

# Multiple Inheritance
class Bat:
    species = "Baty"
    def __init__(self, can_fly=True):
        self.fly = can_fly

    def say(self,msg):
        msg = "..."
        return msg
class Batman(Superhero, Bat):
    def __init(self, *args, **kwargs):
        # Instead of
        # super(Batman, self).__init__(*args, **kwargs)
        Superhero.__init__(self, "anonymous", movie=True, superpowers=["Wealthy"], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        self.name = "Sad Affleck"
    def sing(self):
        return "nananana batman!"
"""
Unpack / Pack
"""

# Unpack tuple
my_func(*(1,2,3,4))            # my_func(1,2,3,4)

# Unpack dict
my_func(**{"a": 3, "b": 4})    # my_func(a=3, b=4)

# Unpack collection into variables
a,b,c = (1,2,3)
a, *b, c = (1,2,3,4) # b = [2,3], c = 4

# Unpack dict into dict
{"a": 1, **{"b": 2}} # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}} # => {'a': 2}

"""
Iterable
"""

# An object that can be treated as a sequence
# More technically, an object that can create an iterator

# ex:
range(5)
my_iterable = {"one": 1, "two": 2}.keys()
list(my_iterable) # => ["one", "two"]
# Loop over iterable
for i in my_iterable:
    print(i)      # 'one' 'two'
    
# No indexing
my_iterable[0]    # Raises TypeError

# Create iterator
my_iterator = iter(my_iterable)

"""
Iterator
"""
# Object that remembers the state as it traverses
next(my_iterator) # => "one"
next(my_iterator) # => "two"
next(my_iterator) # Raises StopIteration
list(my_iterator) # => []

# Loop over iterator
for i in iter(my_iterable):
    print(i)      # 'one' 'two'
    

"""
Exceptions
"""

try:
    raise IndexError("uh oh index error")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    print("All good no exceptions")
finally:
    print("Clean up resources here!")
    
# Instead of try/finally for resource cleanup use a with statement

"""
Files
"""

# Open File
with open("file.txt") as f:
    # Loop each line
    for line in f:
        print(line)

# Read File
with open("file.txt", "r") as f:
    print(f.read())

# Write file
with open("file.txt", "w") as f:
    f.write("baba booey")
    
# Format as JSON
import json
with open("file.txt", "w") as f:
    f.write(json.dumps({"a": 1, "b": 2}))

# Load from JSON
import json
with open("file.txt", "r") as f:
    print(json.load(f))

"""
User Interaction
"""

input("Enter your name")

"""
Modules / 3rd Party Libraries
"""

# Import
import math
math.sqrt(16)

# Import local math.py
# Local files in the same directory have priority
import math

# Import specific functions
from math import ceil, floor
ceil(3.7)  # => 4
floor(3.7) # => 3

# Import all functions
# not recommended
from math import *
print(ceil(3.7))

# Alias
import math as m
m.sqrt(16)

# List functions and attributes
import math
dir(math)

"""
Generators
"""

# Memory-efficient 
# (only load data needed to process the next value)
def double_numbers(iterable):
    for i in iterable:
        yield i + i
        
# range is a generator
for i in double_numbers(range(1,900000000)):
    print(i)
    if i >= 30:
        break
    
# generator comprehension
values = (-x for x in [1,2,3,4,5]) # => <generator object...
for x in values:
    print(x)
my_list = list(values)
