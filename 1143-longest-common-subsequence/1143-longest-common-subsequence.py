class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        def dfs(i: int, j: int):

            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in mem:
                return mem[(i, j)]

            if text1[i] == text2[j]:
                mem[(i, j)] = 1 + dfs(i+1, j+1)
                return mem[(i, j)]
            else:
                increment_text1_pointer = dfs(i+1, j)
                increment_text2_pointer = dfs(i, j+1)
                mem[(i, j)] = max(increment_text1_pointer, increment_text2_pointer)
                return mem[(i, j)]

        return dfs(0, 0)


            
            
            
            

        