class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = self.calculate_set_bits(a)
        s2 = self.calculate_set_bits(b)

        if s1 >= s2:
            return s1*s2
        else:
            return s2//s1 

    
    def calculate_set_bits(self, n: int) -> int:
        count = 0

        while n > 0: 
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count

        