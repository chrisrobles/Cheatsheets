# Files

`import os`

## Handling files proper

```python
with open("test.txt") as line:
    data = line.read()
# OR
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        
with FileManager('test.txt', 'w') as f: # loading a fil
    f.write('Test')

print(f.closed)
```

- Open/read/write/close file:
    ```python
    # Open
    myFile = open(path, mode = r)
    myContents = myFile.read()
    readlines() # list of string values from file
    myFile.close()

    # Write
    open(path, w) # overrides original file contents
    # creates a new file if it doesnt exist
    write('test') 

    # Close
    myFile.close()

    # Append
    open(path, a) # append to the end of the file
    ```
- copy,move,rename,delete:
    `import shutil`
- safe delete:
    `import send2trash`
- Join file path
    `os.path.join('usr', 'bin', 'spam')`
- File size:
    `os.path.getsize(path)`
- Directory
  - Get current working directory
    `os.getcwd()`
  - Change current working directory
    `os.chdir`
  - Get files in dir:
      `os.listdir(path)`
  - Check if it exists:
      `os.path.exists(path)`
  - Check file exists:
      `os.path.isfile(path)`
  - Check dir exists:
    `os.path.isdir(path)`
