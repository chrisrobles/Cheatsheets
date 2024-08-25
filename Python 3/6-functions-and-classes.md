# Functions and Classes

## Functions

```python
def hello():
    print('Hello')

hello()
```
- Typing
  - void 
    - functions return None (null)
  - no method overloading in python
    - (same method name with different types)
  - type enforcement 
    - Python 3.5 >
      - `def multiply(a: int, b: int) -> int:`
    - Python 3.5 <
      - checked with runtime function type()
- *FUNCTIONS ARE OBJECTS*
  - functions can be stored in variables
    - allows to pass to other functions
    ```python
    def my_func():
        print("hey")
    sayHey = my_func  # no `()` means func wont execute, but store in var
    sayHey()
    ```
- Function **nesting** is possible (function defined inside of function)
  - inner function cant be called from outside of outer function
  - inner function can be returned
- Custom Function **Documentation**
    ```python
    def my_func(my_args):
        '''These are the docs'''
        pass # do nothing
    print(my_func.__doc__)  # Output: These are the docs
    ```

### Global Variable

define a global variable in local scope with global keyword

```python
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs) #prints spam
```

### Lambdas / inline functions

```python
add = lambda a,b: a+b
print(add(4,5)) #Output: 9
```

- anonymous function / function w/o name
- infinite parameters
- one expression
- auto returns function object (can store in variable)


## Decorators

<https://stackoverflow.com/questions/5929107/decorators-with-parameters>
<https://www.google.com/search?client=firefox-b-1-d&q=decorator+with+arguments>
<https://www.geeksforgeeks.org/decorators-with-parameters-in-python/>
<https://www.youtube.com/watch?v=MjHpMCIvwsY>
  
- Allow you to change the behavior of a function 
  - without modifying the function
  - run the same code on multiple functions
    - add logging
    - test performance
    - perform caching
    - verify permissions
- How?: its a func that takes a func as a param and calls it in a nested function with code before and after the call potentially
    ```python
    def my_decorator_func(func):
        def wrapper_func(*args, **kwargs):
            # Do something before the function.
            func()
            # Do something after the function.
        return wrapper_func

    @my_decorator_func
    def execute_inside_wrapper():
        pass
    ```
- Example
    ```python
    @mydeco
    def add(a,b):
        return a+b
    
    add(2,2)
    # actually calling mydeco(add)
    ```
- Arguments get passed to the wrapper function inside the `@mydeco` function

#### Decorate every function of a class

This uses a metaclass to automatically decorate all methods of the class with before_every_method_decorator, which runs code before each method call. This approach is more advanced and alters the class creation process, so it's important to understand the implications and how metaclasses work in Python

```python
def before_every_method_decorator(method):
    def wrapper(*args, **kwargs):
        print("This runs before every method call.")
        return method(*args, **kwargs)
    return wrapper

class DecoratorMeta(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        for attribute_name, attribute in dct.items():
            if callable(attribute):
                attribute = before_every_method_decorator(attribute)
            new_dct[attribute_name] = attribute
        return type.__new__(cls, name, bases, new_dct)

class MyClass(metaclass=DecoratorMeta):
    def method_one(self):
        print("Method one.")

    def method_two(self):
        print("Method two.")

obj = MyClass()
obj.method_one()
obj.method_two()
```


## Arguments

### Positional Arguments

*Order matters* when passed positionally

```python
def quadratic(a, b, c):
    x1 = -b / (2*a)
    x2 = sqrt(b**2 - 4*a*c) / (2*a)
    return (x1 + x2), (x1 - x2)

quadratic(31, 93, 62)  # passed POSITIONALLY
```

- Only allow positional args (no keyword args)
    `f(x,y, /)`
  - python 3.8 >
  - left side of `/` can only be defined by positional args
- Unpack list to pass multiple positional args at once
    ```python
    def product(n1, n2):
        #...

    product(*numbers)
    # same as product(numbers[0], numbers[1])
    ```

### Keyword Arguments

Specify parameter name when passing

- *Order doesnt matter* when passed by name / keyword

- Unpack dict to pass multiple keyword args at once
    ```python
    items = {'name': "Trey", 'website': "http://treyhunner.com", 'color': "purple"}
    format_attributes(**items)
    ```
- Required keyword arguments:
  - Capture all positional arguments so the rest of the arguments have to be keywords
    ```python 
    def join(*iterables, joiner): 
        #...
    join(5,2,3)  # error because joiner not passed
    join(5,2,3, joiner=",")

    # iterables catches all positional args 
    # so "joiner" must be defined as keyword arg due to no default value
    ```
- Only allow keyword args (no positional args)
    `def person(*, name, dateOfBirth):`
  - `*` as a parameter
  - right side of * can only be defined by keyword args
- Use both keywords and positional args
    `def foo(a, b, /, *, c, d=5):`
    `foo(1,2,c=3) OR foo(1,2,c=3,d=4)`
  - left side of `/` = forced positional args
  - right side of `*` = forced keyword args
- inspect
  - `get_signature` to see how functions labels args

## Parameters

### Default parameters | Optional Parameters

Parameter is filled by default so dont need define as argument

- **Default Parameters are defined ONCE** 
  - This results in a problem with mutable default arguments
    - The problem is the expression is evaluated once, when the function is defined, and that the same “pre-computed” value is used for each call.
  - Solution:
    ```py3
    def createStudent(name, age, grades=None):
    if grades is None:
      grades = []
    ```

`def print(*strings, sep=' '):  # sep is optional`

### *args | Pack all Positional Arguments into One Parameter

```python
# all positional keywords stored in numbers as tuple
def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total
```

### **kwargs | Pack all Undefined Keyword Arguments into One Parameter
     
```python
def sum(*numbers, **options):
```

## Classes

```python
class fib:
    myVar = "test"  # property / class variable
    def __init__(self):  # constructor
        self.prev = 0  # instance variable
        self.curr = 1
    def __del__(self):  # destructors (called when del myObj)
        pass
    def __iter__(self):  # makes it an iterable
        return self
    def __next__(self):  # makes it usable iterator
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
f = fib()
list(islice(f,0,10)) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Method Types

#### Instance Method

Gets & Sets instance variables / object state

Belongs to the instance

- i.e. member function
- `self` required as first param of every instance method
  - (instance of class) passed automatically as first argument

#### Class Method

Get & Set class state

Belongs to the class

#### Static Method

Belongs to the class but doesnt alter the state of the class

### Access Modifiers

- Public
  - automatic
- Private
  - `__` prefix on member name
- Protected
  - `_` prefix on function name
  - like private, but can be accessed by children

### Function Modifiers

- `@classmethod` decorator
  - implicitly receives the class as an argument
  - When to use?
    - Factory methods (similar to constructor) that will return class objects
- `@staticmethod` decorator
  - Does not implicitly receive the class as an argument
  - Can not access or modify the class state
  - When to use?:
    - Utility Functions
    - Makes sense for the function to be in the class

### Inheritance

```python
class Teacher(Person):  # Teacher extends Person
  def __init__(self, name, age, subject):
    self.subject = subject
    Person.__init__(self,name, age)  # calls the parent constructor to set properties
```

## Objects

- Test if callable:
  - `callable(object)`
  - True if object has `__call__()` method
  - Classes are callable by default
