def repeatedString(s, n):
    if len(s) == 1 and s != 'a':
        return 0
    elif len(s) == 1 and s == 'a':
        return n
    elif len(s) > n:
        return s[:n].count('a')
    else:
        loop_cnt = n // len(s)
        mod_cnt = n % len(s)
        return s.count('a') * loop_cnt + s[:mod_cnt].count('a')
        