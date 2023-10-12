for i in range(len(arr)):
        for j in range(len(arr)):
            if ((arr[i]+arr[j])==m) and (i!=j):
                return [i+1,j+1]