class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        for i in range(x+1):
            z=i*i
            if(x<z):
                return i-1