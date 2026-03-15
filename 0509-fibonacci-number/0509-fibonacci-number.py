class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        if(n==2):
            return 1
        f=1
        s=1
        while(n>=3):
            r=f+s
            f=s
            s=r
            n-=1
        return r