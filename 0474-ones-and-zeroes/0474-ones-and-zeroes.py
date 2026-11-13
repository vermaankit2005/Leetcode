class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        mem = {}
        def dfs(i: int, size_0: int, size_1: int) -> int:

            if i == len(strs):
                return 0

            if (i , size_0 , size_1) in mem:
                return mem[(i , size_0 , size_1)]

            zeros, ones = self.find_zero_ones(strs[i])

            # Include current string, only if it fits
            take = 0
            if size_0 + zeros <= m and size_1 + ones <= n:
                take = 1 + dfs(i + 1, size_0 + zeros, size_1 + ones)

            # Exclude current string
            skip = dfs(i + 1, size_0, size_1)

            mem[(i , size_0 , size_1)] =  max(take, skip)
            return  mem[(i , size_0 , size_1)]

        return dfs(0, 0, 0)


    def find_zero_ones(self, item: str) -> list[int]:
        count_zero = 0
        count_one = 0

        for ch in item: 
            if ch == '0':
                count_zero += 1
            if ch == '1':
                count_one += 1
            
        return [count_zero, count_one]
        
        