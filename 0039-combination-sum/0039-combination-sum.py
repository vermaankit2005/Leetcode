class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(i: int, current_state: List[int], total: int) -> None:

            if i == len(nums) or total > target:
                return
            
            if total == target:
                result.append(current_state.copy())
                return
            

            dfs(i+1, current_state, total)

            current_state.append(nums[i])
            total += nums[i]
            dfs(i, current_state, total)

            total -= nums[i]
            current_state.pop()

        dfs(0, [], 0)
        return result