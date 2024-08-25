# Collections

- empty containers == false

## Indexes/Slices

Indexes enumerate the elements
Slices enumerate the spaces between the elements
```python
Index from rear:    -6  -5  -4  -3  -2  -1      a=[0,1,2,3,4,5]    a[1:]==[1,2,3,4,5]
Index from front:    0   1   2   3   4   5      len(a)==6          a[:5]==[0,1,2,3,4]
                   +---+---+---+---+---+---+    a[0]==0            a[:-2]==[0,1,2,3]
                   | a | b | c | d | e | f |    a[5]==5            a[1:2]==[1]
                   +---+---+---+---+---+---+    a[-1]==5           a[1:-1]==[1,2,3,4]
Slice from front:  :   1   2   3   4   5   :    a[-2]==4
Slice from rear:   :  -5  -4  -3  -2  -1   :
                                                b=a[:]
                                                b==[0,1,2,3,4,5] (shallow copy of a)
                                                b = []
        
                                                b = b.extend(a)
# slice [n:m] 
## [from start index:up to index
example[1:3] #[3.1415, True] SLICE

## SLICE TO END
example[1:] #[3.1415, True, None, 'last']

## SLICE FROM BEGINNING
example[:2] #[['hello', 'world'], 3.1415]

## SLICE to 1 before end
example[1:-1] #[3.1415, True, None]
```

## Strings

### Info functions

```python
# Length
len(myStr)

# substring [from start index:up to index]
"string"[0:2]  # st

# isX
isalpha() # if only letters and is not blank
isalnum() # if only letters and numbers and is not blank
isdecimal() # if only numbers and is not blank
isspace() # if only spaces, tabs, and new lines and is not blank
istitle() # if only words that begin with an uppercase letter followed by only lowercase

# startswith/endswith
'Hello world'.startswith('Hello') #returns true

# convert to ascii
ord(")")

# convert ascii to character
chr(65) # A
```

### Manipulation functions

```python
# Concat
'Alice' + 'Bob'

# Multiply
'Alice' * 5

# type cast
myInt = int(myStr)
str(myInt)  # used for end user / goal to be readable
repr(myInt)  # used for debugging / goal to be unambiguous / will be wrapped in ' '
float(myStr)

# case manipulation
myStr.lower().upper() # lower case returns string object that upper() turns upper case
myStr.title() # title case

myStr.isupper() # has no lowercase and at least one upper
myStr.islower() # has no uppercase and at least one lower

# string to list of WORDS
## default separator = by space
"Hello, World".split()  # ["Hello," , "World"] 
"Hello, World".split(", ")  #["Hello" , "World"]

# string to list of CHARS
list('Hello') # ['H','e','l','l','o']

# escape characters:
\'
\"
\\

# insert tab 
\t = tab

# insert newline
\n = newline

# removing whitespace:
myStr.strip() #return a new string without any whitesapce characters at the beginning or end
myStr.lstrip()
myStr.rstrip()

# move text right, left, or center | justify
txt = "hello"
x = txt.rjust(20)
print(x,"world")
```


## Lists / arrays
- Passes by reference when copied and when used as an argument
- Size is dynamic
- Dont use for
  - Large data sets
    - growing beyond allocated memory will force the entire list to be moved to a new allocated memory slot O(n)
  - Stacks or Queues, use deque
    - i.e if *Inserting* or *deleting* near the ends has a high cost because everything after it must be moved individually O(n-1) = O(n)

```python
example = [['hello', 'world'], 3.1415, True, None, 'last']
```

### Default list
`[0] * 4 # [0,0,0,0]`

### Index

```python
example[0] #['hello', 'world']
example[-1] #'last'

"""
  n  [ 0, 1, 2, 3,   -1 ]
      |  |  |  |   |    |
  m   0  1  2  3 4/-1  5
"""

# slice [n:m] 
## [from start index:up to index
example[1:3] #[3.1415, True] SLICE

## SLICE TO END
example[1:] #[3.1415, True, None, 'last']

## SLICE FROM BEGINNING
example[:2] #[['hello', 'world'], 3.1415]

## SLICE to 1 before end
example[1:-1] #[3.1415, True, None]
```

### Find

- Find Index:
  `example.index('last') # returns 4`

- Find Number of Occurrences:
`example.count('abc')  # of times 'abc' occurs in list`

### In/Not In

```python
'chris' in ['hello', 'world'] #false
'chris' not in ['hello', 'world'] #true

# with error throwing
assert 'chris' in ['hello','world'] #assertion error thrown
assert 'chris' not in ['hello','world'] #nothing returned
```

### Print List

```python
print(*arr) # ['hello', 'world'] 3.1415 True None last
# same as print(' '.join(map(str, arr)))
print(arr) # [['hello', 'world'], 3.1415, True, None, 'last']
```

### Length

`len(examples) #5`

### Concat | Append

```python
list3 = list1 + list2
list1 += list2
list1.append('at the end')
## if a list is passed it will add the list into a single index (creating a 2D list)

# concat per element (separated)
list1.extend(list2)
list1.extend('chris') [...,'c','h','r','i','s']
## adds each element individually
## goes into lists to add each element
```

### Insert

`list1.insert(-1, 'before last')` 
- O(n) operation INEFFICIENT

### Replace

all values in slice range replaced

list1[1:1] = ['hello', 'world']
list1[1:2] = ['Hello,', 'World']

### Delete | Pop

```python
# delete, no return
del example[0]  # can also delete variables

# delete, return value deleted
example.pop()  # last item (top of stack)
example.pop(0)  # first item
```

### Remove by value

`example.remove('hello')`
- throws ValueError if value not found

### Multiple Assignment

```python
cat = ['fat', 'orange']
size, color = cat
# SAME AS size = cat[0]; color = cat[1]
# size = cat[0]
# color = cat[1]
```

### Sort

`spam.sort() #cant use on lists with different types inside`

- Alphabetical:
  `spam.sort(key=str.lower) #uppercase and lowercase separate in ascii`
- Reverse / DESC:
  `spam.sort(reverse=True)`

### Copy

#### Copy by Value

- shallow: 1D list
- deep: 2D list
- !if the list has a list inside use deepcopy
- python 3: foo = bar.copy()

```python
import copy
spam = [...]
cheese = copy.copy(spam)
cheese = copy.deepcopy(spam)
#OR FASTEST SHALLOW (w/o DEEP)
cheese = spam[:]
#OR FASTEST w/ DEEP
cheese = []
cheese.extend(spam)
# will not keep structure of embedded lists
```

#### Copy by Reference:

`a = b`

### List to String

`', '.join(myCat) #string of list vals joined by ,`
or
`string = *myCat`

### String to List

```python
# by word
text.split()

# by line
text.split('\n') #list of entries divided at every \n
```

### List Comprehension

List Expression

```python
newlist = [x**2 for x in fruits if "a" in x]
# [ (expression_on_item) for (item) in (iterable) if (condition)]

# shorthand for
for x in fruits:
  if "a" in x:
    newlist.append(x**2)
```

- Map / apply function to each element in list:
    map(func, list) 
    - returns map object with results
    - turn into list: list(map(...))

- Filter / test function to each element in list:
    filter(func, list)
    - returns filter object with elements that returned true from applying func to
    - turn into list: list(filter(...))

- Reduce / combine function to each pair of elements in list and return one value:
    from functools import reduce
    reduce(func, list)
    multiply=reduce(lambda a,b:a*b,seq)

## Tuples / const arrays

immutable lists (no add or remove)

`eggs = ('hello', 42, 0.5)`

- more memory efficient than lists
- slight higher time efficiency than lists
- Convert:
    tuple(['cat', 'dog', 45])
    list(('cat', 'dog', 5))
    tuple('hello') #('h','e','l','l','o')
- max()
  - requires all values to be same data type
  - if int, max int
  - if string, string at max index
- min()

## Sets / hash table

`thisSet = {"apple", "banana", "cherry"}`

Like a list (uses hash tables) but 
- no indexes
- random order
- no duplicates

- immutable, can add and remove only
  - `.add()`
  - `.remove()`
- only primitive data types and sets can be added

Good for:
- checking if a specific element is contained in the set compared to another set (Highly OPTIMIZED)
- Adding and checking is usually O(1)
  - but true worst case is O(n)

- define empty set
  - `x = set()`
- check if in set
  - `inSet = True if x in mySet else False`
- append to *current* set
  - `set1.update(set2)`
- union into *new* set
  - `set3 = set1.union(set2)`

### Example

```python
# Python program to demonstrate working # of
# Set in Python

# Creating two sets
set1 = set()
set2 = set()

# Adding elements to set1
for i in range(1, 6):
    set1.add(i)

# Adding elements to set2
for i in range(3, 8):
    set2.add(i)

print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")

# Union of set1 and set2
set3 = set1 | set2# set1.union(set2)
print("Union of Set1 & Set2: Set3 = ", set3)

# Intersection of set1 and set2
set4 = set1 & set2# set1.intersection(set2)
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n")

# Checking relation between set3 and set4
if set3 > set4: # set3.issuperset(set4)
    print("Set3 is superset of Set4")
elif set3 < set4: # set3.issubset(set4)
    print("Set3 is subset of Set4")
else : # set3 == set4
    print("Set3 is same as Set4")

# displaying relation between set4 and set3
if set4 < set3: # set4.issubset(set3)
    print("Set4 is subset of Set3")
    print("\n")

# difference between set3 and set4
set5 = set3 - set4
print("Elements in Set3 and not in Set4: Set5 = ", set5)
print("\n")

# checkv if set4 and set5 are disjoint sets
if set4.isdisjoint(set5):
    print("Set4 and Set5 have nothing in common\n")

# Removing all the values of set5
set5.clear()

print("After applying clear on sets Set5: ")
print("Set5 = ", set5)
```

## Dictionaries / associative arrays

- no duplicate keys
  - duplicate keys will update the value
- order doesnt matter for determining equality
- Python 3.7 > dicts are ordered
- Python 3.6 < unordered

```python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size']) # 'fat'
```

- `.keys()` #tuple of k returned
- `.values()` #tuple of v returned
- `.items()` #tuple of k & v returned

- Foreach loop
    ```python
    for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))
    ```
- In ?
    'color' in myCat.keys() #True
    'gray' in myCat.values() #True
- Key In ? w/ no return
    assert 1 in {1: 'foo'} #returns nothing
    assert 'foo' in {1: 'foo'} #assertion error thrown
- Get value
    myCat.get('name', 'cat doesn't have a name')
    1st param: key to get value from
    2nd param: (optional) value to return if key isnt found
- Setdefault / check if key exists and set value if not
    myCat.setdefault('name', 'sam')
    Checks if `name` key exists and if not create it and set it to `sam`
    Returns the key's value
- Pretty Printing 
  - Prints the contents of a dictionary better
    ```python
    import pprint
    pprint.pprint(myCat) #prints
    pprint.pformat(myCat) #returns a string
    ```
- Dict comprehension | Single Line Loop
  - *Dict expression*
  - `{x: x for x in numbers}`
- Zip | Create Dict from 2 Lists
    ```python
    name = [...]
    address = [...]
    mapped = dict(zip(name, address))
    #{"name": "address", "name":...}
    ```
- Combine dictionaries
  - new key-value pairs will be added
  - overlapping keys will be updated
  - `dict1.update(dict2)`

## 3rd Party Collections


`from collections import`

like the built in containers but w/ added stuff

### defaultdict

- dict subclass that calls a factory function to supply missing values
- dict subclass
- doesnt give exception when trying ot access non-existent key (key error)
  - calls a factory function to supply missing values
```python
from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
print(nums['two'])  # prints 0
```

### Namedtuple

Create a tuple with keys

- factory function for creating tuple subclasses with named fields
```python
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('Peter', 'James', '13')
print(s1.fname)
```
    
### deque

optimal version of lists

- fast appends and pops on either end

```python
from collections import deque
#initialization
list = ["a","b","c"]  
deq = deque(list)  
print(deq)
#insertion
deq.append("z")  
deq.appendleft("g")  
print(deq)
#removal
deq.pop()  
deq.popleft()  
print(deq)
```

### ChainMap

- dict-like class for creating a single view of multiple mappings
- combines a lot of dictionaries together and returns a list of dictionaries

**When to use?**
- search through multiple dictionaries at a time


```python
import collections
dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps)
```
    
### Counter

dict subclass for counting occurrences of each value present hashable objects

```python
from collections import Counter
list = [1,2,3,4,3]
answer = Counter()
answer = Counter(list)
print(answer[3]) #prints 2
```

### OrderedDict (not needed in Python 3.7)

- dict subclass that remembers the order entries were added
  - even if the value of the key is changed

```python
from collections import OrderedDict  
order = OrderedDict()  
order['a'] = 1  
order['b'] = 2  
order['c'] = 3  
print(order)
#unordered dictionary
unordered=dict()
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)
```

### UserDict

- wrapper around dictionary objects for easier dict subclassing
    
### UserList

- wrapper around list objects for easier list subclassing
    
### UserString

- wrapper around string objects for easier string subclassing
