def countingSort(arr):
    index_sort = [0] * 100

    for i in arr:
        index_sort[i] += 1

    return index_sort