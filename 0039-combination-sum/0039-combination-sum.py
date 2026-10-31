class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def traverse(current_state: list[int], current_sum: int):
            if current_sum == target:
                copy = current_state.copy()
                sorted_copy = sorted(copy)

                if sorted_copy not in ans:
                    ans.append(sorted_copy)
                return
            
            if current_sum > target:
                return

            for num in candidates:
                current_sum += num
                current_state.append(num)

                traverse(current_state, current_sum)

                current_sum -= num 
                current_state.pop()

        traverse([], 0)
        return ans





        