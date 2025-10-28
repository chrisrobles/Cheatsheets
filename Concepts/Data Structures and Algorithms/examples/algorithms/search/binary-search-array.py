def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (R - L) // 2 + L

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1