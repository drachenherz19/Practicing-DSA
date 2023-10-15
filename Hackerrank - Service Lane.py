def serviceLane(n, width, cases):
    result = []
    for case in cases:
        subarray = width[case[0]:case[1]+1]
        min_w = min(subarray)
        result.append(min_w)
    
    return result