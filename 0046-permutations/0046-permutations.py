class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []

        def dfs(i : int, current_state: list[int]):
            
            if len(current_state) == len(nums):
                result.append(current_state.copy())
                return
            
            for j in nums:
                if j in current_state:
                    continue
                current_state.append(j)
                dfs(i+1, current_state)
                current_state.pop()

        dfs(0, [])
        return result
        