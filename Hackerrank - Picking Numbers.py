def pickingNumbers(a):
    a_set=set()
    abs_list = []
    for i in a:
        a_set.add(i)
    for j in a_set:
        tc_val = a.count(j)+a.count(j-1)
        abs_list.append(tc_val)
    
    return max(abs_list)