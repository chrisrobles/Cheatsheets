# Generators

it waits to be ask to do the *next* iteration

- Generates the next value on the fly rather than storing it all in memory
- Has a yield instead of return
- An instance of the generator can only be used once
    ```python
    myGenerator = createMyGenerator()  # myGenerator can only be used once
    """ """
    for v in createMyGenerator()  
    # createMyGenerator() creates a generator only for the scope of this for loop
    # can call the function again somewhere else
    ```
- Considered iterator (handles creating `__iter()__`)
```python
def createGenerator():
    myList = range(3)
    print("second")  # second
    for i in myList:
        yield i*i  # returns a generator
        print("test")  # prints after each print(i)
myGenerator = createGenerator()
for i in myGenerator:
    print(i)  # first
```

#### yield

returns a generator

yield makes it a function a generator

- When function is called no code is ran (prev, curr = 0,1 not ran when function called)
- waits for __next__ to be called on the generator object to start executing code
  - stops executing after yield ran
  - Order of execution:
    ```python
    #same as the class above
    def fib():
        prev, curr = 0,1
        while True:
            yield curr
            prev,curr = curr, prev + curr
    f = fib()
    list(islice(f, 0, 10)) #islice is an efficient split
    ```
    - f is idle, islice() is idle,
        list() will consume all of its arguments by
        calling next() on the islice() instance which will
        call next() on the f instance
    - yield curr produces value in curr and go idle again
    - islice will produce it because not past 10th value
    - list can add curr's value of 1
    - next iteration will pick up after yield until yield encountered again
    - repeats until list() asks islice() for the 11th value
    - islice() will raise a "StopIteration" exception
    - generator (f) will be garbage collected

```python
numbers = [1,2,3,4,5,6]
lazy_squares = (x * x for x in numbers)  
lazy_squares #<generator object <genexpr> at 0x10d1f5510>
next(lazy_squares) #1
list(lazy_squares) #[4,9,16,25,36]
return ", ".join(  #NO FUCKING CLUE WHAT THIS IS LOL
        f"{param}: {value}" #generator expression
        for param, value in attributes.items()
    )
```

### Generator Expression | Single Line Iterator Creation

Like list comprehension but `( )` instead of `[ ]`

Generator expressions are often used with functions like sum, max, and min
`sum(x**2 for x in range(5))`

```python
g = (x**2 for x in range(3))`

# Iterate
next(g)  # 0
for (v in g):
    print(v)  # 2, 4
next(g)  # StopIteration Error
```
- Hard example
    ```python
    numbers = [1,2,3,4,5,6]
    lazy_squares = (x * x for x in numbers)  
    lazy_squares #<generator object <genexpr> at 0x10d1f5510>
    next(lazy_squares) #1
    list(lazy_squares) #[4,9,16,25,36]
    return ", ".join(  #NO FUCKING CLUE WHAT THIS IS LOL
            f"{param}: {value}" #generator expression
            for param, value in attributes.items()
        )
    ```
- can never get the 1 again! Only can be used/iterated once
- Why use?:
  - Less memory, CPU, & lines of code
- When to use?:
  - Useful when you have a huge set of values you only need to read once
    ```python
    #Instead of this
    def something():
        result = []
        for ... in ...:
            result.append(x)
        return result
    #Do this
    def iter_something():
        for ... in ...:
            yield x
    something = list(iter_something()) #Only if you need a list structure
    ```
- print contents:
    `print(*(f"{s}" for s in ["bar", "test"]))`
  - * = unpacking operator (iterates(i.e. call __next__()) over iterable and assigns each value to a different variable)
    - "itertools" library assists a lot
