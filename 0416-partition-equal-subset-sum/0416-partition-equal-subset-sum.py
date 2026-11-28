class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        total = 0
        for item in nums:
            total += item
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        mem = {}
        # True if can partition else False
        def dfs(i, current_sum) -> bool:

            if current_sum == target:
                return True
             
            if i >= len(nums) or current_sum > target:
                return False
            
            if (i , current_sum) in mem:
                return mem[(i, current_sum)]
            
            mem[(i, current_sum)] = dfs(i+1, current_sum + nums[i]) or dfs(i+1, current_sum)
            return mem[(i, current_sum)]
        
        return dfs(0, 0)

        