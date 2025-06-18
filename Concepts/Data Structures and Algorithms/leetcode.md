# Leetcode

## Shifting

Start at the beginning of the direction you are shifting
- Shifting everything to the left? Start at the left side
- Shifting everything to the right? Start at the right side

## In-place algorithm

Algorithm that doesnt require extra space proportional to the input size.

i.e. dont create another array for storing values, just edit the existing array

**How 2**:
1) Keep a Left pointer and a Right pointer
2) Update `R` w/ O(n) loop
   `for R in range(len(myList))`
3) Move the data at `R` to `L` when condition is met
   `if(myList[L] != myList[R])`

## Get min

If data is sorted, getting min is O(1).

### Static data

If the input is not changing, you can just get the minimum.

### Dynamic data

Use a minimum state stack. Keep track of the minimum state at every entry of input, so that you dont have to find the minimum every time the data changes.

## Combine Linked Lists

<mark> DONT THINK OF LINKED LIST AS ARRAY</mark>

**Once one list runs out**, just set the end to the list with stuff still in it

## Queue

### Queue Simulation

Replace simulation with counting or another mathematical approach

Keep track of the data separate from the queue as a count or separate data structure

Patterns to Recognize:
- queue simulation
- Circular queue problem
- greedy decisions (serve an item to someone only if it matches their preference)

Optimal Solution:
1. Count the number of elements and count their uniqueness / organize into separate data structure(s)
2. Traverse the count or separate data structure(s)

## Simulate DS with another DS

Remember the core principles of the ds 

Examples:
- LIFO
- FIFO
- instant access
- O(1) insert at ends
- O(1) insert in middle

## Recursion

### Factorial

> `5! = 5 * 4 * 3 * 2 * 1`

A useful way of thinking of factorial sequence is that `5! = 5 * 4!`
- do you see how recursion can be used here? just keep calling the same function with the value `-1`

```python
def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num-1)
```

### Fibonacci

```python
from functools import cache

@cache  # memoization - it will cache the results of the function calls so that if the function is called again with the same input it will just return from the cache
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)
```

#### Get time complexity 

O(2^n) - Geometric series, i.e. each term is all the numbers before it multiplied by the common ratio

This example can help you understand how to get time complexity of a binary tree.

![1733445327998](assets/leetcode/1733445327998.png)

1) 1st level is 1 node, 2nd level is 2 nodes, 3rd level there is 4 nodes.
2) The pattern is the number of nodes is 2x / **doubles** the previous level
3) Double at each level means multiple by 2 at each level which means **2^n**

### Reverse Linked List

1. Go to the tail of the linked list and start returning to the previous nodes
2. When returning to the previous nodes, always return the og tail
3. Just update the current node in that specific call to point backwards
- `head.next.next = head`

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # List could be empty, make it base case
        if head is None:
            return None
        # create a variable for the head of this linked list
        newHead = head
        # If there is > 1 node turn it into a sub-problem to sort
        if head.next:
            # change the head to the new head of the reverse linked list
            newHead = self.reverseList(head.next)
            # reverse this node
            head.next.next = head
            head.next = None
        return newHead
```
