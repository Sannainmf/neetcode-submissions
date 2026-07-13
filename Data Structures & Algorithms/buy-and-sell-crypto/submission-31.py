class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        longest = 0
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r

            profit = prices[r] - prices[l]
            longest = max(longest, profit)
            r += 1

        return longest
