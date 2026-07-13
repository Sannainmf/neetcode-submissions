class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        arr = []
        most = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                arr.append(profit)
            

        for i in arr:
            most = max(most, i)

        return most
            
        

