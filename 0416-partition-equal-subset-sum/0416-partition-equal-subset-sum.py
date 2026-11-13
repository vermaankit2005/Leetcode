class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        sum = 0 
        for num in nums:
            sum += num
        
        if sum % 2 != 0:
            return False
        
        target = sum // 2

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


        