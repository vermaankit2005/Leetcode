class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = float('-inf')
        freq = {}
        left = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while (right - left) + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left = left + 1
            
            max_len = max(max_len , (right - left) + 1)
        
        return max_len
