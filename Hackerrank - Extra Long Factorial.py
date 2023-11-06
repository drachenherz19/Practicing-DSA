def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def extraLongFactorials(n):
    value = factorial(n)
    print(value)