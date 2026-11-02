class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        max_so_far = nums[0]
        current_sum = nums[0]

        for i in range(1 , len(nums)):
            current_sum += nums[i]
            current_sum = max(nums[i], current_sum)

            max_so_far = max(max_so_far , current_sum)
            
        return max_so_far


        