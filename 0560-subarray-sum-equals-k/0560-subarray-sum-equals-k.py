class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        premap = {0 : 1}
        _sum = 0
        result = 0
        
        for i in range(len(nums)):
            _sum += nums[i]
            
            if _sum - k in premap:
                result += premap[_sum - k]

            premap[_sum] = premap.get(_sum , 0) + 1 

        return result