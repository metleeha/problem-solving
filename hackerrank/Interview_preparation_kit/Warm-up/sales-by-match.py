def sockMerchant(n, ar):
    pair = {}
    for sock in ar:
        try:
            pair[sock] = pair[sock] + 1
        except:
            pair[sock] = 1
    cnt = 0
    for sock in pair:
        cnt += pair[sock] // 2
        
    return cnt