def quickSort(arr):
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[0] > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left.append(arr[0])
    return left + right