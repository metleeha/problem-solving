from collections import defaultdict

def countTriplets1(arr, r):
    total = 0
    one, two = defaultdict(int), defaultdict(int)
    for a in arr: 
        if a % r == 0:
            total += two[a//r]
            two[a] += one[a//r]
        one[a] += 1
    return total

def countTriplets2(arr, r):
    total = 0
    one, two = defaultdict(int), defaultdict(int)
    for a in arr:
        # 가운데값을 딕셔너리에 저장한다.
        two[a] += 1
    for a in arr:
        # 가운데값을 꺼낸다.
        two[a] -=1
        if a % r == 0:
            # 가운데값을 기준으로 세번째 값과 첫번째 값이 존재한다면 총 가지수에 더해준다.
            # 만약 하나라도 0이라면 더해지지 않는다.
            total += two[a * r] * one[a // r]
        # 첫번째 값으로는 디폴트로 더해준다. 
        one[a] += 1
    return total
