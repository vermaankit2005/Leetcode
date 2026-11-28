class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        m = len(text1)
        n = len(text2)
        # return the length of their longest common subsequence
        @cache
        def dfs(i: int, j: int):
            if i >= m or j >= n:
                return 0

            if text1[i] == text2[j]:
                return  1 + dfs(i+1, j+1)
                
            return max(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)


        
        