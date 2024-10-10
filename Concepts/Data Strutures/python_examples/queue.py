from random import sample
values = sample(range(1,11), 10)

#FIFO
class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0
        return
    def empty(self):
        return False if self.size else True
    def size(self):
        return self.size
    def peek(self):
        return self.top.val
    def push(self, val):
        val = Node(val)
        val.next = self.top
        self.top = val
        self.size += 1
        return
    def pop(self):
        tmp = self.top
        self.top = self.top.next  # what happens when you have an empty list?
        self.size -= 1
        return tmp
    def __str__(self):
        myStr = ""
        tmp = self.top
        while(tmp):
            myStr += " " + str(tmp.val) + "\n"
            tmp = tmp.next
        myStr += "|__|"
        return myStr
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

myStack = Stack()
for val in range(10):
    myStack.push(val)
myStack.pop()
print(myStack)
