"""
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return bool(self.head)

    def append(self, value: int) -> None:
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    def appendleft(self, value: int) -> None:
        new = Node(value)
        if not self.head:
            self.tail = new
        else:
            self.head.prev = new
        self.head = new
            

    def pop(self) -> int:
        if not self.head:
            return -1
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        self.tail = curr
        return self.tail.next.val

    def popleft(self) -> int:
        if not self.head:
            return -1
        temp = self.head.val
        self.head = self.head.next
        return temp
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
"""
        
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def append(self, value: int) -> None:
        temp = self.tail
        if self.tail:
            self.tail.next = self.tail = Node(value)
            self.tail.prev = temp
        else:
            self.tail = self.head = Node(value)
 
    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.head:
            node.next = self.head
            node.next.prev = node
            self.head = node
        else:
            self.head = self.tail = node

    def pop(self) -> int:
        if self.tail is None:
            return -1
        popped = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next.prev = None
            self.tail.next = None
        else:
            self.head = None
        return popped

    def popleft(self) -> int:
        if self.head is None:
            return -1
        popped = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev.next = None
            self.head.prev = None
        else:
            self.tail = None
        return popped
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
d = Deque()
print(d.isEmpty())
print(d.append(10))
print(d.isEmpty())
print(d.appendleft(20))
print(d.popleft())
print(d.pop())
print(d.pop())
print(d.append(30))
print(d.pop())
print(d.isEmpty())