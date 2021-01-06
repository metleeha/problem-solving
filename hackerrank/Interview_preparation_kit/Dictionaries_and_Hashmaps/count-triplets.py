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
        two[a] += 1
    for a in arr:
        two[a] -=1
        if a % r == 0:
            total += two[a * r] * one[a // r]
        one[a] += 1
    return total
