class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        max_sum = float('-inf')
        min_sum = float('inf')

        cur_max_sum, cur_min_sum, total  = 0 , 0, 0

        for item in nums:
            cur_max_sum += item
            cur_min_sum += item
            total += item

            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)

            if cur_max_sum < 0:
                cur_max_sum = 0
            
            if cur_min_sum > 0:
                cur_min_sum = 0
        
        if total == min_sum:
            return max_sum
        
        return max(max_sum , (total - min_sum))

        



        