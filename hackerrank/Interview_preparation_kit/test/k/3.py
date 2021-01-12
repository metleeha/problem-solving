
def solution(start_time, running_time):
    res = set()
    end_time = []

    for i in range(len(start_time)):
        end_time = start_time[i] + running_time[i]

    start_time.sort()
    end_time.sort()
    prev_end = 0

    for i in range(len(start_time)):
        if start_time[i] >= prev_end:
            res.add(start_time[i])
            prev_end = end_time[i]
    
    return len(res)