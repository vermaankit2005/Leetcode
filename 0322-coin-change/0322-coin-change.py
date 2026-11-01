class Solution:
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        mem = {}

        def traverse(index : int, current_state: list[int], current_sum: int) -> int:

            best = float('inf')

            if index >= len(coins) or current_sum > amount:
                return float('inf')

            if current_sum == amount:
                return 0
            
            if (index , current_sum) in mem:
                return mem[(index, current_sum)]
            
            for i in range(index, len(coins)):

                current_state.append(coins[i])
                current_sum = current_sum + coins[i]

                child_answer = traverse(i, current_state, current_sum)
                best = min(best , 1 + child_answer)

                current_state.pop()
                current_sum = current_sum - coins[i]

            mem[(index, current_sum)] = best

            return best
        
        ans = traverse(0, [], 0)
        if ans == float('inf'):
            return -1
        return ans
        