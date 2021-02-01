# using_inbuilt_counter

import collections 

class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)
    
# using_bit_manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count