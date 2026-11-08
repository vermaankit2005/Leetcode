class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        visited = set()
        max_area = -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c] != 0 and (r,c) not in visited:
                    self.area = 0
                    max_area = max(max_area, self.dfs(r, c, visited, grid))

        if max_area == -1:
            return 0

        return max_area

    area = 0

    def dfs(self, r, c, visited, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
            return 0
        
        visited.add((r,c))
        self.area += 1

        self.dfs(r+1, c, visited, grid)
        self.dfs(r-1, c, visited, grid)
        self.dfs(r, c+1, visited, grid)
        self.dfs(r, c-1, visited, grid)

        return self.area
        