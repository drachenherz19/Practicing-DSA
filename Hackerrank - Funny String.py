def funnyString(s):    
    r = s[::-1]
    s_ord = [abs(ord(s[i+1]) - ord(s[i])) for i in range(len(s)-1)]
    r_ord = [abs(ord(r[i+1]) - ord(r[i])) for i in range(len(r)-1)]
    return 'Funny' if s_ord == r_ord else 'Not Funny'