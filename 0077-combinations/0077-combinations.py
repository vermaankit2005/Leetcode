class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        current_path = []
        result = []

        def traverse(i: int, current_path: list[int], result: list[list[int]]):
            if len(current_path) == k:
                result.append(current_path.copy())
                return

            for i in range(i, n):
                current_path.append(i+1)
                traverse(i+1, current_path, result)

                current_path.pop()

        
        traverse(0, current_path, result)
        return result

            
        