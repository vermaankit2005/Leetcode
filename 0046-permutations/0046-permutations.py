class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def traverse(i: int, current_state: list[int]):

            if len(current_state) == len(nums):
                ans.append(current_state.copy())
                return

            for j in range(len(nums)):

                if nums[j] in current_state:
                    continue        
                
                current_state.append(nums[j])
                
                traverse(i+1, current_state)

                current_state.pop() 

        traverse(0, [])
        return ans

        