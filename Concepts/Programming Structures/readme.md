# Programming Styles

## Object-Oriented Programming

[Grokking the Low Level Design Interview Using OOD Principles](https://www.educative.io/courses/grokking-the-low-level-design-interview-using-ood-principles)

Using objects to design and build applications. 

Objects
: Combines data and functionality. Building block of OOP. Example, a person object, a dog object.

### Principles

#### 1. Encapsulation

Bundling the methods and properties in an object, protecting it from the outside

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof!"
```

#### 2. Abstraction

Hiding complex details and showing only what's necessary

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self)
        return "Woof!"
```

#### 3. Inheritance

Child classes and take on the properties and behaviors of a parent class

```python
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal): # Animal = extend Animal class
    def speak(self):
        return "Woof!"
```

#### 4. Polymorphism

Greek for "many forms"

Same method does different things based on the object it is acting on

```python
class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
```

## Procedure Oriented Programming

Programs are designed as blocks of statements to manipulate data

## Functional Programming

Programs are constructed by composing pure functions, where the output depends on the input and does not alter external data or state