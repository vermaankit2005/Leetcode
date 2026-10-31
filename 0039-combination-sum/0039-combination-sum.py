class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def traverse(index: int, current_state: list[int], current_sum: int):
            if current_sum == target:
                ans.append(current_state.copy())
                return

            if current_sum > target:
                return

            for i in range(index, len(candidates)):

                current_sum += candidates[i]
                current_state.append(candidates[i])

                traverse(i, current_state, current_sum)

                current_sum -= candidates[i]
                current_state.pop()

        traverse(0, [], 0)
        return ans





        