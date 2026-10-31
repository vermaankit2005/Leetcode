class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def traverse(current_state: list[int]):

            if len(current_state) == len(nums):
                ans.append(current_state.copy())
                return

            for num in nums:
                if num in current_state:
                    continue

                current_state.append(num)
                traverse(current_state)

                current_state.pop() 

        traverse([])
        return ans

        