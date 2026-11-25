class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(i: int, current_sum: int, current_state: list[int]):
            
            if i >= len(candidates) or current_sum > target:
                return
            
            if current_sum == target:
                result.append(current_state.copy())
                return 
            
            # skip 
            dfs(i+1, current_sum, current_state)

            # Take
            current_sum += candidates[i]
            current_state.append(candidates[i])
            
            dfs(i, current_sum, current_state)
            
            current_sum -= candidates[i]
            current_state.pop()
        
        dfs(0, 0, [])
        return result
        

        