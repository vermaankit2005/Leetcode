class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        mem = {}
        def dfs(i: int, current_sum: int) -> None:
            
            if current_sum == amount:
                return 0
            
            if i >= len(coins) or current_sum > amount:
                return float('inf')

            if (i, current_sum) in mem:
                return mem[(i, current_sum)]
            
            # skip
            skip = dfs(i+1, current_sum)

            # Take
            current_sum += coins[i]
            take = 1 + dfs(i, current_sum)
            current_sum -= coins[i]

            mem[(i, current_sum)] =  min(take , skip)
            return  mem[(i, current_sum)]
        
        result = dfs(0, 0)
        if result == float('inf'):
            return -1
                 
        return result



        