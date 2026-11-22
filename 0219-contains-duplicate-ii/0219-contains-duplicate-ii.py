class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        window = set()
        left = 0
        k = k + 1

        for right in range(len(nums)):
            if (right - left) + 1 > k:
                window.remove(nums[left])
                left = left + 1
                
            if nums[right] in window:
                return True
            
            window.add(nums[right])

        return False
        

        