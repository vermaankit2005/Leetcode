class Solution:
    def reverseBits(self, n: int) -> int:

        power = 31
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += pow(2,power)
            n = n >> 1
            power -= 1
        
        return result
        