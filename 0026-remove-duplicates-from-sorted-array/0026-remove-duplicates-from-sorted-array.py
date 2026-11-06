class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 1

        left = 0
        right = 1
        
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
                continue
            
            left += 1
            nums[left] = nums[right]
            right += 1
        
        return left + 1

        
        