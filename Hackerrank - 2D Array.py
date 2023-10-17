def hourglassSum(arr):
    # Write your code here
    print("arr", arr)
    max_sum = float('-inf')
    temp_array = []
    sum = 0
    
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            temp_array.append(arr[i][j])
            temp_array.append(arr[i][j+1])
            temp_array.append(arr[i][j+2])
            temp_array.append(arr[i+1][j+1])
            temp_array.append(arr[i+2][j])
            temp_array.append(arr[i+2][j+1])
            temp_array.append(arr[i+2][j+2])
            print("temp array", temp_array)
            
            for k in range(len(temp_array)):
                sum += temp_array[k]
            print ("sum", sum)    
            
            if sum > max_sum:
                max_sum = sum
                
            sum = 0
            temp_array = []
            
    print("max_sum", max_sum)
    return max_sum