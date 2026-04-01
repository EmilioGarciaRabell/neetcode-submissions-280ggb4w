class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l,r = 0, 1
        max_profit = 0

        for i in range(len(prices) - 1):
            current_profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, current_profit)
                r += 1
        return max_profit