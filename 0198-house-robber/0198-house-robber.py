class Solution:
    def rob(self, nums: list[int]) -> int:
        mem = {}
        def dp(i: int) -> int:

            max_profit = 0
            if i < 0:
                return 0
            if i in mem:
                return mem[i]

            loot_option_1 = nums[i] + dp(i-2)
            loot_option_2 = dp(i-1)

            max_profit = max(loot_option_1, loot_option_2)
            mem[i] = max_profit

            return max_profit
        
        return dp(len(nums)-1)


        