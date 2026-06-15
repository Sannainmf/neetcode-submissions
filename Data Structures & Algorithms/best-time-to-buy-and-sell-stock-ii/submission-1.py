class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        in every case if r is greater than l, get the difference  
        """

        l = 0
        r = 1
        total = 0

        while r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[l] <= prices[r]:
                diff = prices[r] - prices[l]
                total += diff
                l += 1
                r += 1

        return total

        