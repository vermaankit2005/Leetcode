class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        ans = []
        def traverse(i: int, current_state: list[int]):

            if i > len(nums) - 1:
                ans.append(current_state.copy())
                return
            
            current_state.append(nums[i])
            traverse(i+1, current_state)

            current_state.pop()
            traverse(i+1, current_state)

        traverse(0, [])
        return ans

        