from random import sample
values = sample(range(1,11), 10)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, value):  # at head
        node = Node(value)
        node.next = self.head
        self.head = node
    def insert(self, index, value):  # at index
        currNode = self.head
        prevNode = None
        currIndex = 0
        if not currNode:  # empty list
            self.head = Node(value)
            return
        #from beginning to end
        while currNode:
            if currIndex == index:  # found where to insert
                node = Node(value)
                if prevNode:
                    prevNode.next = node
                else:
                    self.head = node
                node.next = currNode
                return
            # move to next index
            prevNode = currNode
            currNode = currNode.next
            currIndex += 1
        #after end
        if index == currIndex:
            node = Node(value)
            prevNode.next = node
            return
        raise Exception("Index not found in Linked List")
    def delete(self, index):  # at index
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        tmp = self.head
        currIndex = 1
        while tmp.next:
            if currIndex == index:
                tmp.next = tmp.next.next
            tmp = tmp.next
    def length(self):
        length = 0
        currNode = self.head
        while currNode is not None:
            length += 1
            currNode = currNode.next
        return length
    def search(self, val):
        index = 0
        tmp = self.head
        while(tmp):
            if(tmp.data == val):
                return index
            index += 1
            tmp = tmp.next
        return None
    def __str__(self):
        myString = ""
        currNode = self.head
        while currNode is not None:
            myString += str(currNode.data) + "->"
            currNode = currNode.next
        return myString

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

myLL = LinkedList()
for x in values:
    myLL.append(x)
print(myLL)
myLL.insert(10, 99)
print(myLL)
print(myLL.length())
print(myLL.search(99))