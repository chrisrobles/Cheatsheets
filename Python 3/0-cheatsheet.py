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
User Input
"""

input("Enter your name")

"""
Variables
"""

# Naming Convention
# snake_case

# Declarations not allowed
a # => Raise NameError

# Global scope
x = 5           # global
def my_func():
    global y    # global

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
Conditionals
"""

if False:
    pass
elif False:
    pass
else:
    print("this will print")

# Ternary operator
"yay!" if 0 > 1 else "nay!"

"""
Conditional Operators
"""

not True      # => False

True and True # Output: True
True or False # Output: True

# Boolean treated as primitive
True + True   # => 2
False -5      # => -5

# Equality operator
# Applies bool() to both sides
# but returns the original value
0 and 2       # => 0
-5 or 0       # => -5
2 or True     # 2
True or 2     # True

# None, 0, and empty evaluate to False
# All other values are True
bool(None)    # => False
bool(0)       # => False
bool("")      # => False
bool([])      # => False
bool(4)       # => True
bool(-1)      # => True

# True and False are actually 1 and 0
0 == False    # => True
2 > True      # => True
2 == True     # => False

"""
Comparison Operators
"""

# Chaining for checking range / between
1 < 2 < 3     # => True
2 < 3 > 2     # => True

# == vs is
# == checks by value
# is checks by reference

# None is an object, use is for comparison
"etc" is None  # => False

"""
Loops
"""

# For Loop
for animal in ["dog", "cat"]:
    print("{} is an animal").format(animal)
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
    break # stop the loop
    continue # continue to the next iteration

"""
Strings
"""
# Multiline
my_str = """multi
line
string"""

# Concatenation
"Hello" + " " + "world!" # => "Hello world!"
"Hello" * 3              # => "HelloHelloHello"
"Hello" " " "world"      # => "Hello world"

# Index
"Hello"[0] # 'H'

# Length
len("This is a string") # => 16

# f-strings (Python 3.6)
name = "chris"
f"{name} is {len(name)} characters long."

"""
List
"""

li = []

# append(value)
li.append(1)        # [1]
li.append(2)        # [1,2]

# insert(index, value)
li.insert(2, 8)     # [1,2,8]
li.insert(2, 7)     # [1,2,7,8]

# Index
li[0]               # => 1
li[-1]              # => 8
li[10]              # Raises an IndexError
li.index(8)         # => 3 # returns index of value

# Slice
# [start:until:step]
li[1:3]             # => [2,7]
li[2:]              # => [7,8]
li[:3]              # => [1,2,7] 
li[::2]             # => [1,7]
li[::-1]            # => [8,7,2,1] # reverse order

# Pop/Remove
li.pop()            # remove from end
del[1]              # remove by index
li.remove(7)        # remove by value
li.remove(7)        # Raises a ValueError

# Check for existence
1 in li     # => True
li.index(1) # Raises ValueError if not found

"""
Tuples
"""

# Immutable list
tup = (1,2,3)
4,5,6 # => (4,5,6)

tup[0] = 1 # Raises TypeError: 'tuple' object does not support item assignment

"""
Dict
"""

# {key: value} iterable
filled_dict = {"one": 1, "two": 2, "three": 3}

# Key must be immutable type
invalid_dict = {[1,2,3]: "123"} # Raises TypeError: unhashable type
valid_dict = {(1,2,3): "123"}

# Get by key
filled_dict["four"]        # Raises KeyError
filled_dict.get("four")    # => None
filled_dict.get("four", "default")    # => 'default value'

# Set key and value
filled_dict["four"] = 4

# Check for existing key
"four" in filled_dict      # => False

# Set if key not defined
filled_dict.setdefault("four", 4)

# Get all keys
list(valid_dict.keys())   # Python <3.7 = random order, Python 3.7+ = in order

# Get all values
list(valid_dict.values()) # Python <3.7 = random order, Python 3.7+ = in order

# Remove key and value
filled_dict.pop("four")    # Raises KeyError if not found
del filled_dict["four"]    # returns value, Raises KeyError if not found

# Dict Comprehension / One line loop
# {*return* *loop* *condition*}
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}

"""
Sets
"""

# Unique tuple
my_set = {1,1,2,3}     # => {1,2,3}

# Values have to be immutables
invalid_set = {[1], 1} # Raises TypeError: unhashable type: 'list'

# Intersection (overlap)
my_set & {3,4,5}       # => {3,4}

# Union
my_set | {3,4,5}       # => {1,2,3,4,5}

# Difference (only look at left)
my_set - {4,5,6}       # => {1,2,3}

# Symmetric Difference (look at both)
my_set ^ {2,3,4,5,6}   # => {1,6}

# Superset (child)
# Check if all values in left are in right
{1,2} >= {1,2,3}       # => False
# Check if all values in right are in left
{1,2} <= {1,2,3}       # => True

# Check if exists
2 in my_set            # => True

"""
Iterable Helper Functions
"""

# Apply function to each value
map(max, [1,2,3], [4,2,1])           # => [4,2,1]

# Filter out values
filter(lambda x: x > 5, [3,4,5,6,7] ) # => [6,7]

# Copy (by value)
my_copy = my_set.copy()
my_copy is my_set      # => False

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
# Catch both
def my_func(*args, **kwargs):
    pass

# First class functions (functions are treated like variables)
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
add_10(3) # => 13
add_5 = create_adder(5)
add_5(3)  # => 8

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

# Lambda / Anonymous Functions (Use once)
(lambda x: x > 2)(3) # => True

def my_function(a, b):
    return a + b
# Function metadata
my_function.__doc__          # => 'This is a docstring for my_function.'
my_function.__module__       # => '__main__'
my_function.__defaults__     # => None (no default arguments)
my_function.__annotations__  # => {} (no type annotations)
my_function.__globals__      # => {'__name__': '__main__', ...} (global variables)
my_function.__dict__         # => {'__module__': '__main__', ...} (function attributes)
# Function attributes
my_function.__name__        # => 'my_function'
my_function.__qualname__    # => 'my_function' (qualified name)
my_function.__doc__         # => 'This is a docstring for my_function.'
my_function.__module__      # => '__main__' (module name)
my_function.__defaults__    # => None (no default arguments)
my_function.__annotations__ # => {} (no type annotations)
my_function.__globals__     # => {'__name__': '__main__', ...} (global variables)
my_function.__code__.co_argcount # => 2

"""
Class
"""

class Human:
    species = "H. sapiens"      # class attribute
    
    def __init__(self, name):   # constructor (__ denotes special method)
        self.name = name        # instance attribute
        self._age = 0           # instance attribute (_ denotes to use internally)
        
    def sing(self):             # instance method (self is an object of the instance and is passed automatically)
        return "{} sings hallelujah".format(name=self.name)
    
    @classmethod
    def get_species(cls):       # class method (cls is class object)
        return cls.species      # class attributes can be accessed through cls
    
    @staticmethod               # static method (no class or instance object)
    def grunt():                # static methods do not have access to instance or class attributes
        return "*grunts*"
    
    @property                   # getter method (trivial getters and setters not required in python)
    def age(self):
        return self._age
    
    @age.setter                 # allows property to be set
    def age(self, age):
        self._age = age
    
    @age.deleter                # allows property to be deleted
    def age(self):
        del self._age
        
me = Human(name="Chris")
me.sing()
Human.species = "H. sapiens sapiens"  # change class attribute
Human.grunt() # => '*grunts*'
i.grunt()     # => '*grunts*'
del i.age

"""
Inheritance
"""

class Superhero(Human):         # Inherit methods and variables from parent class
    species = "Superhuman"      # override parent's attributes
    
    def _init_(self, name, superpowers=None): 
        self.fictional = True
        if superpowers is None: # default argument assign to none to avoid the same list being shared across instances
            superpowers = ["super strength", "bulletproof"]
        self.superpowers = superpowers
        super().__init__(name)  # call the parent's constructor (inherits age attribute)
    
    def sing(self):             # override parent's method
        return "dun , dun, dun!"

# Check if instance of
sup = Superhero(name="Spider-Man")
if isinstance(sup, Human):      # check if instance of Human or subclass
    print("I am a human")
if type(sup) is Superhero:      # check if instance of Superhero (not subclass)
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
        # Instead of super(Batman, self).__init__(*args, **kwargs)
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
# Iterable is an object that implements __iter__() method

# ex:
# Range
range(5)
# Dictionary
my_iterable = {"one": 1, "two": 2}.items()
# String
my_iterable = "one two"
# List
my_iterable = ["one", "two"]
# Set
my_iterable = {"one", "two"}
# Tuple
my_iterable = ("one", "two")

# Loop over iterable
for i in my_iterable:
    print(i)      # 'one' 'two'

# No indexing or slicing
# No next() method (which is used by iterators)
# If required, convert to list
my_list = list(my_iterable) # => ['one', 'two']

"""
Iterator
"""

# Object that remembers the state as it traverses
# Implements __iter__() and __next__() methods

# An iterable can be converted to an iterator using iter()
my_iterable = ["one", "two"]
my_iterator = iter(my_iterable) # => <list_iterator object at 0x...>

# Use next() to get the next value
next(my_iterator) # => "one"
next(my_iterator) # => "two"
next(my_iterator) # Raises StopIteration
list(my_iterator) # => []

# Loop over iterator
for i in iter(my_iterable):
    print(i)      # 'one' 'two'

"""
Files
"""

# Open File
with open("file.txt") as f:     # with is used to ensure file is closed after use)
    # Loop each line
    for line in f:
        print(line)

# Read File
with open("file.txt", "r") as f:
    print(f.read())             # => read entire file as a string

# Write file
with open("file.txt", "w") as f:
    f.write("baba booey")
    # Format as JSON
    import json
    f.write(json.dumps({"a": 1, "b": 2}))

# Load from JSON
import json
with open("file.txt", "r") as f:
    print(json.load(f))

"""
Modules / 3rd Party Libraries
"""

# Import local math.py
# Local files in the same directory have priority
import math
math.sqrt(16)

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
Decorators
"""

# Wrappers
def my_wrapper(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@my_wrapper               
def my_function(x,y):       
    return x+y              

# equivalent:
# def my_function(x,y):
#   return x+y
# my_function = log_function(my_function)

# Preserve function details of decorated functions
from functools import wraps

def log_function(func):
    @wraps(func) # preserve metadata (docstring, function name, arguments list, etc.) are copied to the wrapper
    def wrapper(*args, **kwargs):
        # Do logging or other pre-processing
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def my_function(x,y):
    return x+y
my_function(1,2)

"""
Generators
"""

# Functions that return an iterator
# Use yield to return values one at a time
# Memory-efficient
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
        
# range is a generator
for i in count_up_to(range(1,900000000)):
    print(i)
    if i >= 30:
        break
    
# generator expression
values = (-x for x in [1,2,3,4,5]) # => <generator object...
for x in values:
    print(x)
my_list = list(values) # => [-1, -2, -3, -4, -5]
