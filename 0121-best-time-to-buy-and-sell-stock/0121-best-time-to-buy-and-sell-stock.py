class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for price in prices:
            smallest = min(smallest, price)
            profit = max(profit, price - smallest)
        return profit
        