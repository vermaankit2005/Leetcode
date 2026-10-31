class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def traverse(n : int, current_state: list[int]):

            if n == len(nums):
                ans.append(current_state.copy())
                return
            
            current_state.append(nums[n])
            traverse(n+1, current_state)


            current_state.pop()
            traverse(n+1, current_state)

        traverse(0 , [])
        return ans


        