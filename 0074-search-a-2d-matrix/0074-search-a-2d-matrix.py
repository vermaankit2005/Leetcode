class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        no_rows = len(matrix)
        no_col = len(matrix[0])

        left = 0 
        right = (no_rows * no_col) - 1

        while left <= right:

            mid = (left + right) // 2
            i = mid // no_col
            j = mid % no_col

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True
        
        return False
        