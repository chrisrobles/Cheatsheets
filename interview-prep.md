# Interview Prep

## Algorithms

### Sort

Insert Sort
```python
"""
1. Iteratively work through array
2. Sort each element one at a time
Use: O(n)/O(n^2) - Mostly sorted data / data continously streaming in
"""
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        my_list = []
        if not pairs:
            return my_list
        my_list.append(pairs[:])
        # Traverse from 1 to len(pairs)
        for i in range(1, len(pairs)):
            # Get end of sorted array
            j = i - 1
            # Insert new value into correct spot
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1
            my_list.append(pairs[:])
        return my_list
```

Merge Sort
```python
"""
1. Recursively split in half until size 1 sub-array
2. Merge L and R half
Use: O(nlogn) - consistentcy
"""
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortInPlace(pairs, 0, len(pairs))
    def mergeSortInPlace(self, pairs, s, e):
        if (e-s) <= 1:
            return pairs
        
        m = (e - s) // 2 + s
        
        self.mergeSortInPlace(pairs, s, m)
        self.mergeSortInPlace(pairs, m, e)

        return self.merge(pairs, s, m, e)
    def merge(self, pairs, s, m, e):
        L = pairs[s:m]
        R = pairs[m:e]
        l = 0
        r = 0
        i = s
        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[i] = L[l]
                l += 1
            else:
                pairs[i] = R[r]
                r += 1
            i += 1
        while l < len(L):
            pairs[i] = L[l]
            l += 1
            i += 1
        while r < len(R):
            pairs[i] = R[r]
            r += 1
            i += 1
        return pairs

```

Quick Sort
```python
"""
1. Choose pivot
2. Move to <= and > with pivot in middle
3. Sort L and R
Use For: Fast and In-place (so good for large datasets / memory constrained environments)
"""
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortInPlace(pairs, 0, len(pairs))
    
    def quickSortInPlace(self, pairs: List[Pair], s, e) -> List[Pair]:
        if (e - s) <= 1:
            return pairs

        # Chooose pivot
        pivot = e - 1
        """
        # Pick median of three (choose between start, end, and median
        pivot = s
        a,b,c = pairs[s].key, pairs[(e + s) // 2].key, pairs[e - 1].key
        if a <= b <= c or c <= b <= a:
            pivot = (e + s) // 2
        elif a <= c <= b or b <= c <= a:
            pivot = e - 1
        """

        # Move less than values to the left of the pivot
        less = s
        for i in range(s, e):
            if pairs[i].key < pairs[pivot].key:
                pairs[less], pairs[i] = pairs[i], pairs[less]
                less += 1
        
        # Move pivot in between
        pairs[less], pairs[pivot] = pairs[pivot], pairs[less]

        # Quick Sort left side
        self.quickSortInPlace(pairs, s, less)
        
        # Quick Sort right side
        self.quickSortInPlace(pairs, less + 1, e)

        return pairs
```

Bucket Sort
```python
"""
1. Create array for range of values
2. First pass through array and update count of each value
3. Second pass through array and sort values
Use for: know range of values
"""
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```

## Leetcode

### Neetcode's Algorithms and Data Structures for Beginners

- Static Arrays
  - [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
  - [27. Remove Element](https://leetcode.com/problems/remove-element/)
- Dynamic Arrays
  - [1929. Concatenation of Array](https://neetcode.io/courses/dsa-for-beginners/3)
- Stacks
  - [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
  - [155. Min Stack](https://leetcode.com/problems/min-stack/description/)
- Singly Linked Lists
  - [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
  - [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)
- Doubly Linked Lists
  - [707. Design Linked List](https://leetcode.com/problems/design-linked-list/description/)
  - [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/description/)
- Queues
  - [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/)
  - [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)
- One-Branch Recursion | Factorial
  - [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
- Two-Branch Recursion | Fibonacci Sequence
  - [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
- Insertion Sort
- Merge Sort
  - [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
- Quick Sort
  - [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/)
- Bucket Sort
- Binary Search | Search Array
  - [704. Binary Search](https://leetcode.com/problems/binary-search/description/)
  - [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)
- Binary Search | Search Range
  - [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/)
  - [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)
  - [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)
- Binary Tree
- Binary Search Tree
  - [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
- BST Insert and Remove
  - [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)
  - [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/description/)
- Depth-First Search
  - [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
  - [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)
  - [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
- Breadth-First Search
  - [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
  - [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)
- BST Sets and Maps
- Backtracking | Tree Maze
  - [112. Path Sum](https://leetcode.com/problems/path-sum/description/)
  - [78. Subsets](https://leetcode.com/problems/subsets/description/)
  - [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)
- Heap / Priority Queue | Heap Properties
- Heap / Priority Queue | Push and Pop
  - [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)
- Heap / Priority Queue | Heapify
  - [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)
  - [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)
  - [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
- Hashing | Hash Usage
  - [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
  - [1. Two Sum](https://leetcode.com/problems/two-sum/description/)
  - [146. LRU Cache](https://leetcode.com/problems/lru-cache/description/)
- Hashing | Hash Implementation
- Graphs | Intro to Graphs
- Matrix DFS
  - [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
  - [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)
- Matrix BFS
  - [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/)
  - [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)
- Adjacency List
  - [133. Clone Graph](https://leetcode.com/problems/clone-graph/description/)
  - [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)
- 1-Dimension DP
  - [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
  - [198. House Robber](https://leetcode.com/problems/house-robber/description/)
- 2-Dimension DP
  - [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/)
  - [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/description/)
  - [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/)
- Bit Operations
  - [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/description/)
  - [338. Counting Bits](https://leetcode.com/problems/counting-bits/description/)
  - [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/description/)


