class Solution:
    def isPalindrome(self, s: str) -> bool:
        mstr = "".join([ch.lower() for ch in s if ch.isalnum()])
        low = 0 
        high = len(mstr) - 1
        
        while low <= high:
            if  mstr[low] != mstr[high]:
                return False
            low += 1
            high -= 1

        return True