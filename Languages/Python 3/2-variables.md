# Variables and Arithmetic

Everything is an object in Python

Every variable is a pointer to an object (`ascii(object)`)

Each object has its own memory allocator

## None / Null

```python
spam
spam == None #True
```

## Swap

a,b = b,a

## Unused Variables

```python
_ = 5
first, _, last = ["first", "get rid of", "last"]  # will get rid of "get rid of"
```

## Get address

Every object has a unique identifier

`id(a)`

## Garbage collection

When no variable points to an object of data the object is orphaned and there is no way to access it.

Python will eventually notice it's inaccessible and reclaim the allocated memory

## Arithmetic Operators

```python
** #Exponent
% #Modulus
// #Floor division
/
*
-
+
```
