class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        _set = set()
        max_len = float('-inf') 
        left = 0

        for right in range(len(s)):
            ch = s[right]

            while ch in _set:
                _set.remove(s[left])
                left += 1
            
            _set.add(ch)
            max_len = max(max_len, (right - left) + 1)
        
        return max_len

            





        