def AppendAndDelete(s, t, k):
    if len(s) + len(t) <= k:
        return 'Yes'
    
    diff_index = min(len(t), len(s))
    # find where they differ
    for i in range(0, min(len(t), len(s))):
        if s[i] != t[i]:
            diff_index = i
            break
         
    ops = k
    ops -= len(s) - diff_index
    ops -= len(t) - diff_index
    
    return 'Yes' if ops >= 0 and ops % 2 == 0 else 'No'