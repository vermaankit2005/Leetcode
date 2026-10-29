class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def traverse(r : int, c: int):
            if r == m - 1 and c == n - 1:
                return 1
            if r > m - 1 or c > n - 1:
                return 0
            
            if (r, c) in mem:
                return mem[(r,c)]
            
            ways_goal = traverse(r + 1 , c) + traverse(r, c + 1)

            mem[(r,c)] = ways_goal
            
            return ways_goal

        return traverse(0, 0)
        





        