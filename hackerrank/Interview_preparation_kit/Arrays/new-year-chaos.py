def minimumBribes(q):
    i = -1
    memo = {}
    while i < len(q)-2:
        i += 1
        i = max(0, i)
        if q[i] == i+1:
            continue
        if q[i] > q[i+1]:
            if memo.setdefault(q[i], 0) == 2:
                print('Too chaotic')
                return
            memo[q[i]] += 1
            q[i], q[i+1] = q[i+1], q[i]
            i -= 2
    print(sum(memo.values()))