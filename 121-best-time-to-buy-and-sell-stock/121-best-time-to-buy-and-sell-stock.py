class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = sell = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                sell = i
                profit = max(profit, prices[sell] - prices[buy])
        return profit