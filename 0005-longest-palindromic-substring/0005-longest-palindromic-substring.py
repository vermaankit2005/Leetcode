class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = float('-inf')
        result = [0, 0]

        for i in range(len(s)):
            odd_len = 0

            # Odd Palindrome check
            l, r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if l == r:
                    odd_len += 1
                else:
                    odd_len += 2
                if odd_len > max_len:
                    max_len = odd_len
                    result[0] = l
                    result[1] = r
                l -= 1
                r += 1

            even_len = 0
            # Odd Palindrome check
            l, r = i , i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                even_len += 2
                if even_len > max_len:
                    max_len = even_len
                    result[0] = l
                    result[1] = r
                l -= 1
                r += 1
        
        return s[result[0]: result[1]+1]




        