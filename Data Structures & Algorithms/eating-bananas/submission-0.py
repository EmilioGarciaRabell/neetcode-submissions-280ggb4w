class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        res = r

        while r >= l:
          k = (l+r)//2

          total_hours = 0
          for p in piles:
            total_hours += math.ceil(float(p)/k)

          if total_hours > h:
            l = k + 1
          else:
            res = k
            r = k - 1
        return res