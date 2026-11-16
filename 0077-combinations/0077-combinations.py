class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        current_path = []
        result = []
        
        nums = []
        for i in range(1, n+1):
            nums.append(i)

        def traverse(i: int, current_path: list[int]):
            
            if len(current_path) == k:
                result.append(current_path.copy())
                return
            
            if i >= len(nums):
                return

            traverse(i+1, current_path)

            current_path.append(nums[i])
            traverse(i+1, current_path)
            current_path.pop()

        traverse(0, current_path)
        return result

            
        