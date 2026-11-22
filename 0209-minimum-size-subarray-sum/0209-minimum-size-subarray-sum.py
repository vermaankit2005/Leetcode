class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        min_len = float('inf')
        left, cur_sum = 0 , 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(min_len, (right-left)+1)
                cur_sum -= nums[left]
                left += 1
            
        # if min_len == float('inf'):
        #     return 0
        # else: 
        #     return min_line

        return 0 if min_len == float('inf') else min_len