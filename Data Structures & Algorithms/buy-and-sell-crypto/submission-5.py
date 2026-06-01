class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        profit = 0
        for i in range(len(prices) -1 ):

            print(r)
            if prices[r] < prices[l]:
                l = r
                

            elif prices[r] > prices[l]:
                current_profit = prices[r] - prices[l]
                profit = max(profit, current_profit)
            r += 1
    
        
        return profit