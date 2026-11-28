class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        mem = {}
        def dfs(i: int):
            if i == len(s):
                return True
            
            if i in mem: 
                return mem[i]

            for j in range(i, len(s)):
                substr = s[i: j+1]

                if substr not in wordDict:
                    continue
                
                
                if dfs(j+1):
                    mem[i] = True
                    return True
            
            mem[i] = False
            return False
        
        return dfs(0)