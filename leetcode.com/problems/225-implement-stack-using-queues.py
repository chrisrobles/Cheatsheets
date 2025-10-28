class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.back = None
    def push(self, x:int) -> None:
        if not self.back:
            self.front = self.back = Node(x)
            return
        self.back.next = Node(x)
        self.back = self.back.next
    def pop(self) -> int:
        if not self.front:
            return -1
        temp = self.front.val
        if self.front == self.back:
            self.back = None
        self.front = self.front.next
        return temp
    def top(self) -> int:
        if not self.front:
            return -1
        return self.front.val
    def size(self) -> int:
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
    def empty(self) -> bool:
        return self.front is None
class MyStack:
    def __init__(self):
        self.s_top = Queue()
        self.rest = Queue()

    def push(self, x: int) -> None:
        if not self.empty():
            self.s_top.front.next = self.rest.front
            self.rest.front = self.s_top.front
            self.s_top = Queue()
        self.s_top.push(x)

    def pop(self) -> int:
        if not self.rest.empty():
            self.s_top.push(self.rest.pop())
        return self.s_top.pop()

    def top(self) -> int:
        return self.s_top.top()

    def empty(self) -> bool:
        return self.s_top.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()