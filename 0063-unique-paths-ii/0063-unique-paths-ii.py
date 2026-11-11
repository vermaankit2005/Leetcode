class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        mem = {}
        def traverse(r : int, c: int):
            
            if obstacleGrid[r][c] == 1:
                return 0
            if r < 0 or c < 0:
                return 0
            if r == 0 and c == 0:
                return 1
            
            if (r, c) in mem:
                return mem[(r,c)]
            
            ways_goal = traverse(r - 1, c) + traverse(r, c - 1)

            mem[(r,c)] = ways_goal
            
            return ways_goal

        return traverse(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        