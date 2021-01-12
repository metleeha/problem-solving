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
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY items
#  2. INTEGER orderBy
#  3. INTEGER orderDirection
#  4. INTEGER pageSize
#  5. INTEGER pageNumber
#

def solution(items, orderBy, orderDirection, pageSize, pageNumber):
    # 0 이름 1 관련도 2 가격
    if orderBy == 0:
        items.sort(key=lambda x:x[orderBy], reverse=orderDirection)
    else:
        items.sort(key=lambda x:int(x[orderBy]), reverse=orderDirection)

    total = len(items) // pageSize 
    start = pageSize * pageNumber
    end = pageSize * pageNumber + pageSize
    
    if end // pageSize == total :
        page = items[start:]
    else:
        page = items[start:end]
    
    res = [p[0] for p in page]
    return res
