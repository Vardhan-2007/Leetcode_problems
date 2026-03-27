class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        elif n==4:
            return False
        else:
            s=0
            while(n>0):
                s+=((n%10)**2)
                n//=10
            return self.isHappy(s)