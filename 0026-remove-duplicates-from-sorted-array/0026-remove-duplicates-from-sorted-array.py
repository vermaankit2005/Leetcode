class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[left] == nums[right]:
                right += 1
                continue
            
            left += 1
            nums[left] = nums[right]
        
        return left+1



        


        
        