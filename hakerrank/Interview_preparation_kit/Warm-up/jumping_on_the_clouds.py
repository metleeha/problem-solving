def jumpingOnClouds(c):
    final = len(c) - 1
    check = 0
    answer = 0
    
    while(check < final):
        if check + 2 <= final and c[check + 2] == 0:
            check += 2
            answer += 1
        elif c[check + 1] == 0:
            check += 1
            answer += 1
    return answer