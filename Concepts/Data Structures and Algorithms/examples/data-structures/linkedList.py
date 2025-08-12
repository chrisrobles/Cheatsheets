class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        while curr:
            if index == 0:
                return curr.val
            index -= 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        while curr:
            # If at index
            if index == 0:
                # Create node and update its pointers
                node = Node(val)
                node.prev = curr.prev
                node.next = curr

                # Update previous node's pointers
                curr.prev = node
                if node.prev:
                    node.prev.next = node
                    
                # Update head if necessary
                if self.head == curr:
                    self.head = node
                break
            index -= 1
            curr = curr.next
        if curr is None and index == 0:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        while curr:
            if index != 0:
                curr = curr.next
                index -= 1
                continue
            if curr.next:
                curr.next.prev = curr.prev
            if curr.prev:
                curr.prev.next = curr.next
            if self.head == curr:
                self.head = curr.next
            if self.tail == curr:
                self.tail = curr.prev
            break
    
    def traverse(self):
        curr = self.head
        index = 0
        while curr:
            print(index, ":", curr.val)
            index += 1
            curr = curr.next
        print("Head:", self.head.val if self.head else None)
        print("Tail:", self.tail.val if self.tail else None)

class DoublyLinkedListDummy:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        # Traverse the list to find the index
        curr = self.head.next
        while curr != self.tail:
            if index == 0:
                return curr.val
            index -= 1
            curr = curr.next
        # Index out of bounds
        return -1

    def addAtHead(self, val: int) -> None:
        # Create new node with pointers
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        
        # Update current nodes
        node.next.prev = node
        node.prev.next = node

    def addAtTail(self, val: int) -> None:
        # Create new node with pointers
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev

        # Update current nodes
        node.prev.next = node
        node.next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr:
            if index == 0:
                # Create new node with pointers
                node = Node(val)
                node.next = curr
                node.prev = curr.prev
                
                # Update current nodes
                node.prev.next = node
                node.next.prev = node
                break
            curr = curr.next
            index -= 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr != self.tail:
            if index == 0:
                # Update nodes
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                break
            curr = curr.next
            index -= 1
    
    def traverse(self):
        curr = self.head
        index = 0
        while curr:
            print(index, ":", curr.val)
            index += 1
            curr = curr.next
        print("Head:", self.head.val if self.head else None)
        print("Tail:", self.tail.val if self.tail else None)
        curr = self.tail
        while curr:
            print(index, ":", curr.val)
            index -= 1
            curr = curr.prev


