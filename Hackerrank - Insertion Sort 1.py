def insertionSort1(n, arr):
    value = arr[-1]
    sorted_arr = sorted(arr)
    
    for i in arr[-2::-1]:
        if arr == sorted_arr:
            break
        elif i > value:
            arr[arr.index(i) + 1] = i
        else:
            arr[arr.index(i) + 1] = value
        print(*arr)
    else:
        if arr != sorted_arr: 
            arr[0] = value
            print(*arr)