# Loops

## Loop Operators

- break = break Loop
- continue = jump back to start of loop
- pass = does nothing just keeps going forward like normal

## while

```python
while condition :
  code
```

## do while

```python
while True:
  print(i)
  i = i + 1
  if i > 3:
    break
```

## range

```python
range(5)  # => 0,1,2,3,4
```

## for

Think of it like an iterator function

```python
#for
for i in range(5):
  print('Jimmy Five Times ' + str(i))

#foreach
for n in numbers:
  print(n)
  # break would prevent the else from running
else:  # optional
  print("Loop Finished")

```