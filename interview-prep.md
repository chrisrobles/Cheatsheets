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

"""
```
### Search
