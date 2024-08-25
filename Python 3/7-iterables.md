# Iterable

aka Sequence

Anything that has a `__iter()__` method

ex. strings, lists, tuples, ...


### Iterable vs Iterator

- Iterable = overall ds can iterated with `__iter__()` / has iterator 
- Iterator = object that produces the next value when you call its `__next()__` method

### Iterable

`myList` is the iterable, an object that has the iterator protocol `__iter__()`

- `__iter__()` returns an iterator
  - an object with `__next()__`
  - could just return self if self has `__next__()`
- ex. string, list, tuple, set, range(), file
- values stored in memory

### Iterator

Any object that has a `__next__()` method

1. Gets an iterator of `myList`
   1. Call `iter(myList)`
   2. Returns object with a `__next__()` method
2. Use the iterator to loop over items
   1. Keep calling `__next__()`
   2. which returns result into `x`
      - if a `StopIteration` is raised from within `__next__()`, it means there are no more values in the iterator and the loop is exited

### Iterable Functions

- Map | apply function to each element in list
  - `map(func, list)`
  - returns map object with results
  - convert to list `list(map(...))`
- Filter | applies function to each element of list that meets condition
  - `filter(func, list)`
  - returns filter object with elements that returned true
  - convert to list `list(filter(...))`
- Reduce | apply function to each pair of elements in list and return one value
    ```python
    from functools import reduce
    reduce(func, list)
    multiply=reduce(lambda a,b:a*b,seq)
    ```
- Zip | take 0 or more iterables and make an iterator of ith tuples
  - `zip(*iterables)`
  - and stops at the length of the shortest iterable
  - ex) iterable1[0] AND iterable2[0] stored in the 0th tuple
- All True?
  - `all(iterable)`
- Any True?
  - `any(iterable)`
  - Often used with generators on lists
    - `any(letter == 't' for letter in 'monty')  # True`
- Reverse Iterator
  - `reversed(seq)`
  - Prereqs
    - seq has a __reversed__()
    - OR
    - *Sequence Protocol* supported
  - __len__()
  - __getitem__()
  - w/ int args starting at 0
    - returns a reverse iterator


## yield

yield will return only when `__next__()` called on object

```python
for iterator in iterable[1:]:
    yield joiner
    yield from iterable
```

## * operator

depends what it is put on

### variable assignment, argument

unpacking operator

- assigns a value from an iterable to a sequence of variables
  - if returning 1 value, just returns a value
  - else returning > 1 value, returns a list of values

```python
# unpack list
arr = [1,2,3]
print(*arr) #Output: 1 2 3 INSTEAD OF [1, 2, 3]
## same as ' '.join(map(str, arr))

# unpack iterable into multiple variables
first, *middle, last = [1, 2, 3, 5, 7] # first = 1, middle = [2,3,5] last = 7

# unpack iterable into single variable
*string, = 'PythonIsTheBest' #['P', 'y', 't', 'h', 'o', 'n', 'I', 's', 'T', 'h', 'e', 'B', 'e', 's', 't']
```

### parameter

packing operator

- pack several values in a single tuple

```python
myFunc(1, "a")

def myFunc(*allParams):
  print(allParams) # (1,'a')
```

## ** unpacking operator for dictionaries

can use inside callables and other dictionaries

`merged_dict = {**food, **colors}`


## Iteration

```python
for x in myList:
    # ...
```