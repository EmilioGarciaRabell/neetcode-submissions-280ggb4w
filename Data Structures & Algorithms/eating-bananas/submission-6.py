import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l = 1
        r = max(piles)

        res = r
        while r >= l:
            k = (r + l)//2
            
            total = 0
            for p in piles:
               total += math.ceil(float(p)/k)

            if total <= h:
               res = k 
               r = k - 1
            else:
                l = k + 1
        
        return res