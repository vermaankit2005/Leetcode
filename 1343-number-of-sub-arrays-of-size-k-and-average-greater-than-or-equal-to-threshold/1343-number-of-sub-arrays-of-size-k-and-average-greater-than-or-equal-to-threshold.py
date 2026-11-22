class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        win_sum = 0
        left = 0
        count = 0 

        for right in range(len(arr)):

            win_sum += arr[right]
            
            if (right - left) + 1 > k:
                win_sum -= arr[left]
                left += 1

            if (right - left) + 1 == k:
                if win_sum // k >= threshold:
                    count += 1
        
        return count



        