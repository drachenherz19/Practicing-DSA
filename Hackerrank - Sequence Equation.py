def permutationEquation(p):
    D, S = dict(), list()
    for i in range(len(p)):
        D[p[i]] = i+1
    I = int()
    for e in range(len(p)):
        I = D[e + 1]
        I = D[I]
        S.append(I)
    return S