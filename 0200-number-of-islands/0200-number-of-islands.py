class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if int(grid[r][c]) != 0 and (r,c) not in visited:
                    count += 1
                    self.dfs(r, c, visited, grid)

        return count
        
    
    def dfs(self, r, c, visited, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or int(grid[r][c]) == 0:
            return
        
        visited.add((r,c))

        self.dfs(r+1, c, visited, grid)
        self.dfs(r-1, c, visited, grid)
        self.dfs(r, c+1, visited, grid)
        self.dfs(r, c-1, visited, grid)
