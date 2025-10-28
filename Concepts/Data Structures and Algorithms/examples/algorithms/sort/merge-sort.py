# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        # Sort Left
        left = self.mergeSort(pairs[:len(pairs) // 2])

        # Sort Right
        right = self.mergeSort(pairs[len(pairs) // 2:])

        # Combine
        l = 0
        r = 0
        for i in range(len(pairs)):
            if l >= len(left):
                pairs[i] = right[r]
                r += 1
            elif r >= len(right):
                pairs[i] = left[l]
                l += 1
            elif left[l].key <= right[r].key:
                pairs[i] = left[l]
                l += 1
            else:
                pairs[i] = right[r]
                r += 1
        return pairs
    