class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        def max_loot(n : int) -> int:
            if n < 0:
                return 0

            if n in memo:
                return memo[n]
                       
            max_loot_at_n = max(max_loot(n-1), nums[n] + max_loot(n-2))

            memo[n] = max_loot_at_n

            return max_loot_at_n
        
        return max_loot(len(nums) - 1)

        