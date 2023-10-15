def marsExploration(s):
    counter = 0
    sos = ["S", "O", "S"]

    for i in range(len(s)):
        ele = sos[i%3]
        if s[i] != ele:
            counter += 1

    return counter