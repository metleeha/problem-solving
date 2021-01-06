def checkMagazine(magazine, note):
    words = {}
    for i in range(m):
        if magazine[i] not in words.keys():
            words[magazine[i]] = 1
        else:
            words[magazine[i]] += 1
    
    for i in range(n):
        if note[i] not in words.keys():
            return 'No'
        else:
            words[note[i]] -= 1
            if words[note[i]] < 0:
                return 'No'
    return 'Yes'