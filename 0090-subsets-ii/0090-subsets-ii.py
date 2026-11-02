class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        current_state = []

        def traverse(i: int, current_state: list[int], result: list[list[int]]):

            if i == len(nums):
                result.append(current_state.copy())
                return
            
            current_state.append(nums[i])
            traverse(i+1, current_state, result)

            current_state.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            traverse(i+1, current_state, result)
        
        traverse(0, current_state, result)
        return result
        