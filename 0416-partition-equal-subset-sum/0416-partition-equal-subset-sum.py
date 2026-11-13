class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        summ = sum(nums)
        
        if summ % 2 != 0:
            return False
        
        target = summ // 2

        mem = [[None] * target for _ in range(len(nums))]

        def dfs(i: int, total: int):
            if total > target:
                return False
            if total == target:
                return True
            if i >= len(nums):
                return False
            if mem[i][total] is not None:
                return mem[i][total]
            
            mem[i][total] = dfs(i+1, total + nums[i]) or dfs(i+1, total)
            return mem[i][total]
        
        return dfs(0, 0)


        