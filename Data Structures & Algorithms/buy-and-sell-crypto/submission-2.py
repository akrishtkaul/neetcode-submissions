class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        l = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[l]:
                profit = max(prices[i] - prices[l], profit)

            else:
                l = i
        
        return profit

        