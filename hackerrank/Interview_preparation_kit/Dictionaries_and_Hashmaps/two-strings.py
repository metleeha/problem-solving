def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    
    return ('YES' if s1.intersection(s2) else 'NO')