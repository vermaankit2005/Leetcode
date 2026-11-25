class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current_state = []
        candidates.sort()
        def dfs(i: int, current_sum: int):

            if current_sum == target:
                result.append(current_state.copy())
                return 
            
            if i >= len(candidates) or current_sum > target:
                return

            # Take
            current_sum += candidates[i]
            current_state.append(candidates[i])
            
            dfs(i+1, current_sum)
            
            current_sum -= candidates[i]
            current_state.pop()
            
            # skip
            while i < len(candidates) -1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, current_sum)

        
        dfs(0, 0)
        return result
        