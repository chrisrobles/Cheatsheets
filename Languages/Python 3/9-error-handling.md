# Error Handling

```python
try:
    # Throw Exceptions
    if False:
        raise Exception("It's false")
    else if False && False:
        raise ValueError("Not proper value")
    # Catch Exceptions
    print(42/0)
    print("This will never print")
except ZeroDivisionError:  # catch
    print('cant divide by 0')
except:  # default
    print('Some error happened')
finally:  # always executes
    print('Always prints')

# ...

assert podBayDoorStatus == 'closed', 'The pod bay doors need to be closed.'
# AssertionError: The pod bay doors need to be closed.
```

- traceback errors 
  - `import traceback`
