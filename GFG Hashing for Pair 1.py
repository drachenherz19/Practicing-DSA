def sumExists(arr, N, sum):
    #Your code here
    setter=set()
    for i in arr:
        setter.add(i)
    for i in arr:
        difference = sum - i
        if difference == i:
            continue
        if difference in setter:
            return 1
    return 0 