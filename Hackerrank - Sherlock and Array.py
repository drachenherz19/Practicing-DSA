def balancedSums(arr):
    is_balanced = 'NO'
    
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        if left_sum != total_sum - left_sum - num:
            left_sum += num
        else:
            is_balanced = 'YES'
            break
    
    return is_balanced