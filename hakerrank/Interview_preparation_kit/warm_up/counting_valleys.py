def countingValleys(steps, path):
    valley_num = 0
    level = 0
    
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        else:
            if level == 0:
                valley_num += 1
            level -= 1
    return valley_num