class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = [0] * 26
        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for num in letters:
            if num != 0:
                return False
        
        return True
            


        