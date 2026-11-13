class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        mem = {}
    
        def dfs(i: index, total: int) -> int:
            
            count = 0
            if i > len(nums):
                return 0
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in mem:
                return mem[(i, total)]
            
            count += dfs(i+1, total + nums[i])
            count += dfs(i+1, total - nums[i])

            mem[(i, total)] = count
            return count
        
        return dfs(0, 0)




        