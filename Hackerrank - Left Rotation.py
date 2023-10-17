def rotLeft(a, d):
    # Write your code here
    new_array = a[d:]+a[:d]
    return new_array