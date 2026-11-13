class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        mem = {}
        # Return the fewest number of coins
        # that means min (no of coins from each side)
        def dfs(i : int, current_sum: int) -> int:

            if i == len(coins) or current_sum > amount:
                return float('inf')
            
            if current_sum == amount:
                return 0
            
            if (i, current_sum) in mem:
                return mem[(i, current_sum)]

            take = 1 + dfs(i, current_sum + coins[i])
            skip = dfs(i+1, current_sum)
            

            mem[(i, current_sum)] =  min(skip , take)
            return mem[(i, current_sum)]

        result = dfs(0, 0)

        if result == float('inf'):
            return -1
        
        return result
        
        