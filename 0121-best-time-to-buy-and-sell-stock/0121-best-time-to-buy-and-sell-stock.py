class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        max_profit = 0
        
        for amount in prices:
            x = min(x, amount)
            max_profit = max(max_profit, amount -x)
        return max_profit
      