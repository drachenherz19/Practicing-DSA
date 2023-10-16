def getTotalX(a, b):
    big=  max(b)
    sma = min(a)
    count = 0
    for i in range(1, big+1):
        if all(i%j == 0 for j in a) and all(k%i == 0 for  k in b):
            count += 1
                        
    return count