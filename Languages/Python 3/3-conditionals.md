# Conditionals

Conditional statements that evaluate to either True or False

## Logical Operators

```python
and
or
not
is not None
```

## Bool

False = 
- False
- 0
- None
- empty (container)
- ""

False does not equal to -1

## if statement

```python
if condition :
    code
elif condition :
    code
else :
    code
```

### If Expression | Ternary Operator

`[on_true] if [expression] else [on_false]`

## switch statement 

[Python 3.10 or higher](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching)
    
```python
match subject:
    case <pattern_1>:
        <action_1>:
    case <pattern_2>:
        <action_2>:
    case <pattern_3>:
        <action_3>:
    case _:
        <action_default>
```

## Special Operators

### is

is two variables the same object in memory

```python
a = 1
b = 1
a is b # False
b = a
a is b # True
```

### in
```python
myList = [1,2,3]

# If statement (check value is in iterable)
if 3 in myList: # True

# Loop statement (iterate and get value from list)
for x in myList: 
  print(x) # 1 2 3
```
- can check for a list inside a list
