class Solution:
    def rob(self, nums: list[int]) -> int:
        mem = {}
        def dp(i: int) -> int:

            if i < 0:
                return 0
            if i in mem:
                return mem[i]

            mem[i] = max(nums[i] + dp(i-2) , dp(i-1))
            return mem[i]
        
        return dp(len(nums)-1)


        