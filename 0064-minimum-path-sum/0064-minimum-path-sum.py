class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        mem = {}
        # return min path sum
        def dfs(row, col) -> int:
            if row < 0 or col < 0 : 
                return float('inf')
            
            if row == 0 and col == 0:
                return grid[0][0]
            
            if(row, col) in mem:
                return mem[(row, col)]
 
            mem[(row, col)] = grid[row][col] + min(dfs(row-1 , col), dfs(row, col-1))
            return mem[(row, col)]
        
        return dfs(len(grid) - 1, len(grid[0]) - 1)