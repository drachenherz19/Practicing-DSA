def pangrams(s):
    s = s.lower()
    letter = 'abcdefghijklmnopqrstuvwxyz'
    unique_letter = set(s) # only give unique letter in set
    for char in letter:
        if char not in unique_letter:
            return "not pangram"
    return "pangram"