def sherlockAndAnagrams(s):
    total = 0
    chars = {}
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            chunk = ''.join(sorted(s[j:j+i]))
            total += chars.setdefault(chunk, 0)
            chars[chunk] += 1
    return total