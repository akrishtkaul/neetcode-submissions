class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftIndex = 0
        rightIndex = 1
        max_profit = 0 

        while rightIndex < len(prices):
            if prices[leftIndex] < prices[rightIndex]:
                profit = prices[rightIndex] - prices[leftIndex]
                max_profit = max(max_profit, profit)
            else:
                leftIndex = rightIndex 

            rightIndex += 1
        return max_profit


        