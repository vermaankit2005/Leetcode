class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0 

        for item in nums:
            cur_sum += item
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
            
        
        return max_sum


        