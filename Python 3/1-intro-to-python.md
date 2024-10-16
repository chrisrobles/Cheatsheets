# Intro to Python

<mark>EVERYTHING IS OBJECTS</mark>

Python is an interpreted, object oriented, scripting language

Tips:
- follows indentation to separate code blocks instead of flower brackets `{}`
- dynamically typed

## REPL

`$ python`
`>>> print("hello world")`
`hello world`

Read, Evaluate, Print, and Loop Python code using direct communication with the Python Interpreter

i.e. type in Python code and get the results displayed immediately

## Boilerplate

```python
# defined starting point
# allows to import and run program in another script
def main():
  print("hello world")

# only runs if program ran independently
if __name__ == '__main__': 
  main()
```

## Comments

```python
# comment
"""
multi
line
comment
"""
```

## Print

```python
# Spaces
print('Hello, World!')
print('Hello,', 'World!')
print('Hello', end=', '); print('World!')  # end parameter default = '\n' (new line)

# Line breaks
print('Hello,')
print('World!')

print('Hello,') ; print('World!')

# Multiline strings
print('''
Hello,
World!
''')

# Variables
world = "World"
print(f'Hello, {world.title()}!')
print('Hello, {}!'.format(world))
print('Hello, {person}!'.format(person=world))
print("Hello, ", world, "!")

# Raw string
print(r'Hello \t World \n !')  # Hello \t World \n !
```

### Printing to Debug

Use logpoints instead

Prints to the console and doesnt stop program

## Input

`myInput = input("Message to user: ")`

- Dynamic Input
  ```python
  catNames = []
  while True:
      name = input()
      catNames = catNames + [name]
      if name == "exit":
          break
  ```

