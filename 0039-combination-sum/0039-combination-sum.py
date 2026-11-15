class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(i: int, current_state: List[int], sum: int) -> None:

            if i == len(nums):
                return
            
            if sum == target:
                result.append(current_state.copy())
                return
            
            if sum > target:
                return
            
            dfs(i+1, current_state, sum)

            current_state.append(nums[i])
            sum += nums[i]
            dfs(i, current_state, sum)

            sum +- nums[i]
            current_state.pop()

        dfs(0, [], 0)
        return result