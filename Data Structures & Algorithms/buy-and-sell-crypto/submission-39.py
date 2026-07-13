class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        mostProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l
            
            profit = prices[r] - prices[l]
            mostProfit = max(mostProfit, profit)
            r += 1

        return mostProfit

        