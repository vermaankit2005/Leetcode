class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_state = []

        def traverse(i: int, current_state: list[int], result: list[list[int]]):

            if i == len(nums):
                result.append(current_state.copy())
                return
            
            current_state.append(nums[i])
            traverse(i+1, current_state, result)

            current_state.pop()
            traverse(i+1, current_state, result)
        
        traverse(0, current_state, result)
        return result




        


        