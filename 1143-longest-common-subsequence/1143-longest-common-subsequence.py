class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        # return the length of their longest common subsequence
        def dfs(i: int, j: int):
            
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i , j) in mem:
                return mem[(i, j)]

            if text1[i] == text2[j]:
                mem[(i, j)] =  1 + dfs(i+1, j+1)
                return mem[(i, j)]
            
            mem[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return mem[(i, j)]
        
        return dfs(0, 0)


        
        