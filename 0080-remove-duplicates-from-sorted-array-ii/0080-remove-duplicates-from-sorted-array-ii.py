class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        left = 0
        right = 0
        allowed = True
        for right in range(1, len(nums)):
            
            if nums[left] == nums[right]:
                if allowed:
                    left += 1
                    nums[left] = nums[right]
                    allowed = False
                continue
            
            left += 1
            nums[left] = nums[right]
            allowed = True
        
        return left + 1
            


            


        

        