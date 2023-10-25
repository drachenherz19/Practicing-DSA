def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    w = (size*4)-3
    rows = (size*2)-1
    for i in range(0, rows):
        index = abs(size-(i+1))
        n = size-(index+1)
        m = (n*2)+1
        a = ''
        for j in range(m):
            c = abs(n-j)+index
            a = '-'.join([alphabets[c],a])
        print(a.center(w, '-')[:w])