# Context Managers

ensures that resources are returned after usage

## Using `With`

```python
with open("test.txt") as line:
    data = line.read()
# returns resources after with statement exits
```

## Creating from Scratch

- `__enter__()`
  - returns the resource that needs to be managed
- `__exit__()`
  - no return, performs cleanup

```python
class ContextManager():
    def __init__(self):
        print('init method called')
        
    def __enter__(self):
        print('enter method called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')
print("Last thing to be printed")
```
