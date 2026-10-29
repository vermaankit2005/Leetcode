class Solution:
    mem = {}
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        if n in self.mem:
            return self.mem[n]
        
        fib_n = self.fib(n-1) + self.fib(n-2)

        self.mem[n] = fib_n
        return fib_n
        
        