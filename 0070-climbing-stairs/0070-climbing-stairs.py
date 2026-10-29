class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}
        def traverse(current_stair: int) -> int:

            if current_stair == n:
                return 1

            if current_stair > n:
                return 0

            if current_stair in memo:
                return memo[current_stair]
            
            result  = 0 

            for step in [1, 2]:
                current_stair = current_stair + step
                
                result = result + traverse(current_stair)
                
                current_stair = current_stair - step
            
            memo[current_stair] = result
            return result

        return traverse(0)
        
