# Data Structures

> A way to store data in an efficient manner inside of RAM

## Array

Ordered, contiguous group of elements.

Useful to:
- Access something with a known location instantly
- Add to the end of a ds(stack)

### Static Arrays

Cannot change size after initialization.

Default in *strictly typed languages*.
- Java
- C++
- C#

#### Read/Write - O(1)

```python
myArray = [1,3,6]
myArray[0]     # 1 / O(1)
myArray[1] = 1 # 1 / O(1)
```

#### End - O(1)

Insert O(1) - Assuming the array isnt full, you can instantly insert into the array at the end
```python
def insertEnd(arr, numValues, val):
    if numValues < len(arr):
        arr[numValues] = val # insert after last value
```

Delete O(1) - Simply making it represent an empty space, as you wouldnt deallocate the memory since it's a fixed size.s
```python
def deleteEnd(arr, numValues):
    if numValues > 0:
        arr[numValues-1] = 0 # delete last value
```

##### Middle - O(n)

Insert & Delete - 

Cant set the value to a default value because it will break the contiguous order.

So we must shift everything.

Worst case the insert / delete is at the beginning, and you would have to shift everything.

```python
def insertMiddle(arr, i, val):
    for index in range(len(arr)-1, i, -1):
        arr[index] = arr[index-1]
    arr[i] = val
def deleteMiddle(arr, i):
    for index in range(i, len(arr) - 1): # -1 b/c you dont want to grab +1 after the last index 
        arr[index] = arr[index+1]
    arr[-1] = 0 # make the end of the array a default value
```

### Dynamic Arrays

Can change size and keeps track of the last element in the array with a pointer

Default in *loosely typed languages*
- Python
- PHP
- JS

#### Complexity

| Read | Insert / Delete Ends | Insert / Delete Middle |
| --- | --- | --- |
| O(1) | Amortized Ω(1) | O(n) |

> Amortized - average time per operation
> > Use to ensure the average performance is acceptable, even if some individual operations might take longer

#### Reallocate - O(n)

When the array gets too big for its allocation, it reallocates a bigger array (usually double) in memory. (Also it deallocates the old array.)

Reallocating happens so infrequently the O(n) time complexity for reallocating isnt really a concern. So, the amortized complexity (average) of pushing to the end of an array is still Ω(1).

The fact that reallocating happens so infrequently so its not worth worrying about is proven using [Power Series](https://medium.com/@erkmenefe/a-comprehensive-guide-to-arrays-understanding-static-dynamic-arrays-and-ram-storage-255226aed0c7).

#### Example

```python
class DynamicArray: 
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if(i < self.length):
            return self.arr[i]
        raise IndexError("Out of bounds")

    def set(self, i: int, n: int) -> None:
        if(i < self.length):
            self.arr[i] = n
        
    def pushback(self, n: int) -> None:
        if(self.length == self.capacity):
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.arr = self.arr + [0]*self.capacity
        self.capacity *= 2

    def getLength(self) -> int:
       return self.length

    def getCapacity(self) -> int:
        return self.capacity
```

## Stack

LIFO - Last in First out

Tips:
- Implement with list
- If keeping track of properties of the data in the stack (min, etc.), consider creating a second stack to track the property as the stack updates.
  - Every time you push to the main stack, push to the second stack.
  - That way you have the property(minimum) at each state of the stack.
  - If you just kept track of the minimum, once the minimum got popped you would have to do O(n) operations to find the minimum again vs. if you just popped from the minimum stack.

Useful to:
- reverse sequences
  - recursion goes in reverse because it pops off the call stack

Examples:
- Pre / Post Order Operations (56+ i.e. 5 + 6)
- Work on to do list by starting with smallest task

### Complexity

| Push | Pop | Peek |
| --- | --- | --- |
| Add to top | Remove from top | Read from top |
| O(1)       | O(1)            | O(1)          |

## Linked List

Ordered sequence of nodes w/ a value and next pointer

Tips:
- <mark>DONT THINK OF A LINKED LIST AS AN ARRAY</mark>
  - focus on each node as an individual
  - non-contiguous
  - stored randomly in RAM
- Create a dummy node at head and just return head.next
  - This allows you to avoid checking if a linked list is empty when point .next to it

Useful To:
- Insertion and deletion

Examples:
- Power Point slideshow easy insert in the middle

### Complexity

| Access | Search | Insert | Delete |
| --- | --- | --- | --- |
| O(n) | O(n) | O(1) | O(1) |

### Code

```python
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def get(self, i: int) -> int:
        curr = self.head
        while curr and i:
            i -= 1
            curr = curr.next
        if curr:
            return curr.val
        return -1
    def insertHead(self, val: int) -> None:
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        if not self.tail:
            self.tail = self.head
    def insertTail(self, val: int) -> None:
        tmp = Node(val)
        if self.tail:
            self.tail.next = tmp
        self.tail = tmp
        if not self.head:
            self.head = self.tail
    def remove(self, i: int) -> bool:
        prev, curr = None, self.head
        while curr and i:
            i -= 1
            prev = curr
            curr = curr.next
        if not curr: # Index out of bounds
            return False
        # Guaranteed to be 1 length
        if not curr.next: # Tail
            self.tail = prev
        if not prev: # Head
            self.head = self.head.next
        else:
            prev.next  = prev.next.next
        return True
    def getValues(self) -> List[int]:
        myList = []
        curr = self.head
        while curr:
            myList.append(curr.val)
            curr = curr.next
        return myList
```

## Doubly Linked List

Linked list with an added `prev` pointer

Tips:
- f

Useful to:
- build stack

Examples:
- f

### Time Complexity

Access: O(n)
Search: O(n)
Insertion at known: O(1)
Deletion at known: O(1)

### Example

```python

def update_decorator(func):
    def wrapper(linked_list_instance, *args, **kwargs):
        print(f"{func.__name__}({', '.join(map(str, args))}) ")
        # Call the original method (like 'add' or 'remove')
        result = func(linked_list_instance, *args, **kwargs)
        
        # After calling the original method
        linked_list_instance.traverse()
        
        return result
    return wrapper
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        curr = self.head
        while i != index:
            i += 1
            curr = curr.next
        return curr.val
    
    @update_decorator
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        if not self.length:
            self.tail = new
        else:
            self.head.prev = new
        self.head = new
        self.length += 1
    
    @update_decorator
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.prev = self.tail
        if not self.length:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.length += 1
    
    @update_decorator
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if(index == 4 and val == 3):
            print(self.length)
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        i = 0
        curr = self.head
        
        while i != index:
            i += 1
            curr = curr.next
        new = Node(val)
        new.next = curr
        new.prev = curr.prev
        new.prev.next = new
        curr.prev = new
        self.length += 1
    
    @update_decorator
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        i = 0
        curr = self.head
        while i != index:
            i += 1
            curr = curr.next
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        curr.prev = None
        curr.next = None
        self.length -= 1
        
    def traverse(self) -> None:
        curr = self.head
        print(self.length, end=" ")
        while curr:
            extra = ""
            if(curr == self.head):
                extra += "H"
            if(curr == self.tail):
                extra += "T"
            print(extra + str(curr.val),end="->")
            curr = curr.next
        print("")

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1,4)
obj.addAtTail(8)
obj.addAtHead(5)
obj.addAtIndex(4,3)
obj.addAtTail(0)
obj.addAtTail(5)
obj.addAtIndex(6,3)
obj.deleteAtIndex(7)
obj.deleteAtIndex(5)
obj.addAtTail(4)
```

## Queues

FIFO | "First come first serve"

*use linked list*

<mark>Queue should be empty at end to be valid</mark>

Useful for:
- Removing from the beginning O(1)
  - Arrays cant do that because it would need to shift everything
- breadth first search

### Enqueue - O(1)

Enter queue at `tail`

```python
def enqueue(self, val):
    newNode = ListNode(val)

    # Queue is non-empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    # Queue is empty
    else:
        self.left = self.right = newNode
```

### Dequeue - O(1)

Remove from queue at `head`
- Check it's not empty first

```python
def dequeue(self):
    # Queue is empty
    if not self.left:
        return None
    
    # Remove left node and return value
    val = self.left.val
    self.left = self.left.next
    if not self.left:
        self.right = None
    return val
```

## Deque | "deck"

Double-ended queue

Add and remove from both ends

```python
def update_decorator(func):
    def wrapper(deque_instance, *args, **kwargs):
        print(f"{func.__name__}({', '.join(map(str, args))}) ")
        # Call the original method (like 'add' or 'remove')
        result = func(deque_instance, *args, **kwargs)
        
        # After calling the original method
        deque_instance.traverse()
        
        return result
    return wrapper
class Deque: 
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False
    
    @update_decorator
    def append(self, value: int) -> None:
        new = Node(value)
        if self.isEmpty():
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new
        
    @update_decorator
    def appendLeft(self, value: int) -> None:
        new = Node(value)
        if self.isEmpty():
            self.head = new
            self.tail = new
            return
        self.head.prev = new
        new.next = self.head
        self.head = new
        
    @update_decorator
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return temp
    
    @update_decorator
    def popLeft(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return temp
    
    def traverse(self) -> None:
        curr = self.head
        while curr:
            extra = ""
            if(curr == self.head):
                extra += "H"
            if(curr == self.tail):
                extra += "T"
            print(extra + str(curr.value),end="->")
            curr = curr.next
        print("")
        
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
       
myDeq = Deque() 
myDeq.isEmpty()
myDeq.append(10)
myDeq.isEmpty()
myDeq.appendLeft(20)
myDeq.popLeft()
myDeq.pop()
myDeq.pop()
myDeq.append(30)
myDeq.pop()
myDeq.isEmpty()
```

## Binary Tree

### Time Complexity

1) 1st level is 1 node, 2nd level is 2 nodes, 3rd level there is 4 nodes.
2) The pattern is the number of nodes is 2x / **doubles** the previous level
3) Double each at each level means multiple by 2 at each level which means **2^n**
4) Since we have to traverse to the last level, it is **O(n)**
