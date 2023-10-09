def insertionSort2(n, arr):
    for i in range(1, n):
       
        curr_ele = arr[i]
        count = 0
        
        if curr_ele < arr[i-1]:
            for j in range(i, 0, -1):
                
                if curr_ele < arr[j-1]:
                    arr[j] = arr[j-1]
                    arr[j-1] = curr_ele
                else:
                    break
    
        print(" ".join(map(str, arr)))