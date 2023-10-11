def countingSort(arr):
    index_sort = [0] * 100

    for k in arr:
        index_sort[k] +=  1

    j = 0
    for i in range(len(index_sort)):
        if index_sort[i] > 0:
            temp = index_sort[i]

            for _ in range(temp):
                arr[j] = i
                j += 1

    return arr