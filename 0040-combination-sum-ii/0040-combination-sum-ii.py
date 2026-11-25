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
            
            j = i
            # skip
            while j < len(candidates) -1 and candidates[j] == candidates[j+1]:
                j += 1
            dfs(j+1, current_sum)

            # Take
            current_sum += candidates[i]
            current_state.append(candidates[i])
            
            dfs(i+1, current_sum)
            
            current_sum -= candidates[i]
            current_state.pop()
        
        dfs(0, 0)
        return result
        