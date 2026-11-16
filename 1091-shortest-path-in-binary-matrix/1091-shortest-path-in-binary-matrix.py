from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1 or grid[len(grid) -1][len(grid[0]) - 1]:
            return -1

        que = deque()
        que.append((0, 0))
        visited = set()
        visited.add((0, 0))
        length = 1

        navigate = [(0, 1), (0 , -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        while que:
            for _ in range(len(que)):
                r, c = que.popleft()
                
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length

                for i , j in navigate:
                    dr = r + i
                    dc = c + j

                    if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]) and (dr, dc) not in visited and grid[dr][dc] == 0:
                        que.append((dr, dc))
                        visited.add((dr, dc))
                
            length += 1
        
        return -1





