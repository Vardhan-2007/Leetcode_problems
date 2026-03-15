class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        f=0
        s=1
        while(n>=2):
            r=f+s
            f=s
            s=r
            n-=1
        return r