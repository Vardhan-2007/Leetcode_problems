class Solution:
    def climbStairs(self, n: int) -> int:
        f=0
        s=1
        while(n!=0):
            r=f+s
            f=s
            s=r
            n-=1
        return r