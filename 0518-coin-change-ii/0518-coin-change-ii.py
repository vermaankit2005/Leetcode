class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        mem = {}
        
        # Return the number of combinations that make up that amount
        def dfs(i : int, current_sum: int) -> int:

            if current_sum == amount:
                return 1

            if i == len(coins) or current_sum > amount:
                return 0
            
            if (i, current_sum) in mem:
                return mem[(i, current_sum)]

            take = dfs(i, current_sum + coins[i])
            skip = dfs(i+1, current_sum)
            
            mem[(i, current_sum)] =  take + skip
            return mem[(i, current_sum)]

        return dfs(0, 0)
        