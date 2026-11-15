class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def dfs(i: index, current_state: list[int]):

            if i == len(nums):
                result.append(current_state.copy())
                return
            
            current_state.append(nums[i])
            dfs(i+1, current_state)

            current_state.pop()
            dfs(i+1, current_state)
        
        dfs(0 , [])

        return result
            

        