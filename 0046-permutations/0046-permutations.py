class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_state = []
        mem = {}
        def dp() -> None: 

            if len(current_state) == len(nums):
                result.append(current_state.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in current_state:
                    continue
                current_state.append(nums[j])
                dp()
                current_state.pop()
            
        dp()
        return result