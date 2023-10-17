def makeAnagram(a, b):
    # Write your code here
    count = 0
    total_len = len(a) + len(b)
    for i in a:
        if i in b:
            count+=1
            b = b[:b.index(i)] + b[b.index(i)+1:]
    return total_len - (count * 2)