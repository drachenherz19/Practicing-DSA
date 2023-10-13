def beautifulDays(i, j, k):
    beautiful_days = 0
    for i in range(i,j+1):
        reversed_value = int(str(i)[::-1])
        if abs(i-reversed_value)%k == 0:
            beautiful_days += 1
    return beautiful_days