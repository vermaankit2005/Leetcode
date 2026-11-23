class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = float('-inf')
        freq = {}
        left = 0

        for right in range(len(s)):
            
            freq[s[right]] = freq.get(s[right], 0) + 1

            while (right - left) + 1 - self.find_max_freq(freq) > k:
                freq[s[left]] -= 1
                left = left + 1
            
            max_len = max(max_len , (right - left) + 1)
        
        return max_len


    def find_max_freq(self , freq: dict) -> int:
        max_freq = 0
        for value in freq.values():
            max_freq = max(max_freq, value)
        return max_freq
