class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        for i in range(len(nums)):
            val = abs(nums[i])

            if nums[val] < 0:
                return val
            
            nums[val] = -1 * nums[val]
        
        return -1