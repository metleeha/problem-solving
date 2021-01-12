#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
from collections import defaultdict
def solution(arr):

    # Write your code here
    account = defaultdict(int)
    
    for i in range(len(arr)):
        Min = 9999
        taker = arr[i][0]
        giver = arr[i][1]
        point = arr[i][2]
        
        account[taker] -= int(point)
        account[giver] += int(point)

    Min = min(account.values())
    
    if Min >= 0:
        return  [ "None" ]
    else:
        res = [key for key in account if account[key] == Min]
        return sorted(res)
if __name__ == '__main__':