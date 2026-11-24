class Solution:
    def climbStairs(self, m: int) -> int:
        mem = {}
        def solve(n: int):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return n
            
            if n in mem:
                return mem[n]
            
            mem[n] = solve(n-1) + solve(n-2)
            return mem[n]
        
        return solve(m)
        
        