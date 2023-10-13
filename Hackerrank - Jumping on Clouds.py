def jumpingOnClouds(c, k):
    e = 100
    idx = 0

    while True:
        idx = (idx + k) % n 
        
        if c[idx] == 1:
            e -= 3
        else:
            e -= 1

        if idx == 0:
            break
    return e