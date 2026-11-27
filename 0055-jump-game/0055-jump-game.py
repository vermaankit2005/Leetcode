class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        max_range = nums[0]
        
        for i in range(1, len(nums)):
            if i > max_range:
                return False
            
            max_range = max(max_range, i + nums[i])
        
        return True




        