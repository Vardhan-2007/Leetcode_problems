class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        if(n==2):
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)