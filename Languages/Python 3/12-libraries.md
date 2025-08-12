# Libraries

## Virtual Environment

Allows to create multiple Python environments with different modules and packages

**Recommended that you always use Python virtual environments and not install additional Python packages direct into your Python installation**

New virtual environment
1. Create a virtual environment
   - Windows:
     1) `py -3 -m venv .venv`
     2) `.venv\scripts\activate`
     3) if "Activate.ps1...", change PowerShell execution policy to allow scripts to run
         1) Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   - macOS/Linux:
     1) `python3 -m venv .venv`
     2) `source .venv/bin/activate`
2. Install packages inside venv
3. Add `.venv/` to .gitignore
4. Create list of dependencies
   - `pip freeze > requirements.txt`

Existing virtual environment
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

VSCode
- Prompted when a new virtual environment created "Set as default for your workspace folder?"
- If yes, Environment automatically activated when you open a new terminal

### Commands

- deactivate
    `$ deactivate`

## Standard Library | stl

[Standard Library](https://docs.python.org/3/library/)

- Modules written in C to give access to the system Python doesnt have
  - standardized solutions to common problems in programming
  - enhance portability by abstracting away platform-specifics into platform-neutral APIS

### Command Line arguments

```python
import sys
sys.argv[1]
```

### Random

```python
import random, sys, os, math
random.randint(1,10)
# OR
from random import * #from random import everything
randint(1,10) #didnt need to specify random. because of from
sys.exit()

# GET HELP
help(randint)
```


## 3rd Party Libraries

Install
- Windows:
  1. In the python directory, under scripts folder
  2. ./pip.exe install pyperclip
  - OR
  1. `python -m pip install pyperclip # may require elevation`
- macOS:
  - `python3 -m pip install pyperclip`
- linux:
  - `apt-get install python3-tk`
  - `python3 -m pip install pyperclip`

### Copy & Paste

```python
import pyperclip
pyperclip.copy('test')
pyperclip.paste()
```

### Save variables to hard drive

```python
import shelve
myFile = shelve.open('mydata')
cats = ['sophie', 'pooka', 'Simon']
myFile['cats'] = cats
myFile.close()
```

### math

```python
import math
print(math.sqrt(16))
```

### matplotlib

`import matplotlib.pyplot as plt`

- wont show on wsl

### pandas

working with large datasets

### numpy

`import numpy as np`

complex math and common statistical operations

### logging logs


### Asyncio | Concurrent Execution | Asynchronous I/O

[Distribute tasks via queues](https://docs.python.org/3/library/asyncio.html)

`import asyncio`
    
### Multiprocessing
    
[Process-based Parallelism](https://docs.python.org/3/library/multiprocessing.html)
    
`import multiprocessing`
    
- Spawns processes by 
  1. side-stepping the Global Interpreter Lock
     - *Global Interpreter Lock* assures CPython only has one thread execute Python bytecode
  2. using subprocesses instead of threads
        
- When to use:
  - for CPU heavy processes that dont benefit from threading
  - Programs that need more CPU

- How to:
  - create a process
    - `from multiprocessing import Process`
  - offer a convenient means of parallelizing the execution of a function across multiple input values
    - `from multiprocessing import Pool`
  - Threading
    - a thread is an execution context (all the info needed to execute / resume executing a stream of instructions)
    - two things appearing to be happening at once
      - but threads dont run at the same time
      - even if they are on different processors
    - When to use?:
      - Tasks that spend much of their time waiting for external events
      - NOT for CPU-bound problem
        - NOT for processes that require heavy CPU computation and spend little time waiting for external events might not run faster at all.
      - Want tasks to run simultaneously and not have to wait on each other i.e. CONCURRENCY
      - takes far less time to create & terminate a thread than to create a new processes
      - can share common data, they do not need to use inter-process communication
      - slower than context switching
    - Example:
        A web browser will need multiple threads
        1) Display the page
        2) Download files
        ...
        If you only had one thread, the web page could not display while the download is happening 
    - multiprocessing vs threading
      - A program running is called a process
      - A program can have multiple processes
      - A process can have multiple threads
    - Process vs Thread:
      - A process has data
      - A thread has a stack, registers, and the program counter
    - Subprocess
      - run & control other programs

## Security Considerations

[More info](https://docs.python.org/3/library/security_warnings.html)

- base64, cgi, hashlib, http.server, logging, multiprocessing, pickle
  random, shelve, ssl, subprocess, tempfile, xml, zipfile

## CPython

Python is compiled into instructions (bytecode), then it's ran on a virtual machine 

- Types are represented by a struct called PyObject which every object in Python uses
  - Contains 2 attributes
    1. ob_refcnt (reference count)
    2. ob_type (pointer to another type)