class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a)
        b=int(b)
        r1=0
        r2=0
        r3=""
        count=0
        while(a!=0):
            r1+=((2**count)*(a%10))
            count+=1
            a//=10
        count=0
        while(b!=0):
            r2+=((2**count)*(b%10))
            count+=1
            b//=10
        sum=r1+r2
        if(sum==0):
            r3+='0'
        while(sum!=0):
            r3+=str(sum%2)
            sum//=2
        return r3[::-1]