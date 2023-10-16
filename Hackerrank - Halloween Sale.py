def howManyGames(p, d, m, s):
    count = 0

    while s >= m and s>=p:

        if p <= m:
            s -= m
            print(s)
            count += 1
        else:
            s -= p
            p = p - d
            count += 1


    return count