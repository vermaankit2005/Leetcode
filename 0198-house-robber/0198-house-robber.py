class Solution:
    def rob(self, nums: list[int]) -> int:
        mem = {}
        def dp(n: int):

            if n >= len(nums):
                return 0
            
            if n in mem:
                return mem[n]
            
            take = nums[n] + dp(n+2)
            skip = dp(n+1)

            mem[n] = max(take , skip)
            return mem[n]

        return dp(0)
            

        