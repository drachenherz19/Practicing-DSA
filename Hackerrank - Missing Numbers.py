def missingNumbers(arr, brr):
    freq_brr = {i: 0 for i in set(brr)}
    freq_arr = {i: 0 for i in set(arr)}
    for i in brr:
        freq_brr[i] += 1

    for i in arr:
        freq_arr[i] += 1

    missing_numbers = []
    for i in freq_brr.keys():
        if freq_brr.get(i) != freq_arr.get(i):
            missing_numbers.append(i)

    return missing_numbers