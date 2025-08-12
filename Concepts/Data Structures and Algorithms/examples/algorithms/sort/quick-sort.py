# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    def quickSortHelper(self, pairs: List[Pair], start: int, end: int) -> None:
        # Base Case - one or no elements
        if (end - start + 1) <= 1:
            return
        
        # Recursive Case - partition into < and >=
        pivot = end # last element = pivot
        left = start
        for i in range(start, end):
            # Swap < to be left
            if pairs[i].key < pairs[pivot].key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        # Swap pivot
        pairs[left], pairs[pivot] = pairs[pivot], pairs[left]
        # Sort left and right
        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, end)