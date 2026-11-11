class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_so_far = float('inf')
        max_profit = 0

        for price in prices:
            if min_so_far > price:
                min_so_far = price
            
            max_profit = max(max_profit, price - min_so_far)
        
        return max_profit