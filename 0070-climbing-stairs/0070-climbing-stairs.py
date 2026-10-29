class Solution:
    mem = {}
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 1
        if n < 0:
            return 0

        if n in self.mem:
            return self.mem[n]

        ways_n = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.mem[n] = ways_n

        return ways_n

        


        