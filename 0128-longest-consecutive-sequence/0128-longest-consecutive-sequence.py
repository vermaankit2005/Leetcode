class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        nums.sort()

        max_overall = 1
        current = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] + 1 == nums[i+1]:
                current += 1
            elif nums[i] == nums[i+1]:
                while i < len(nums) -1 and nums[i] == nums[i+1]:
                    i += 1
                continue
            else:
                current = 1
                
            max_overall = max(max_overall, current)
            i += 1
            
        return max_overall

            

        