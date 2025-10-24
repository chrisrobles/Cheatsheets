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

### Search
