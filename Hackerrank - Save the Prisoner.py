def saveThePrisoner(n, m, s):
    res = (m % n + (s - 1)) % n
    return res or n