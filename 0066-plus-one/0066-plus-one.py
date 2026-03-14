class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)-1
        sum=0
        count=0
        for i in digits:
            sum+=(i*(10**(l-count)))
            count+=1
        sum+=1
        l1=[]
        while(sum!=0):
            l1.insert(0,sum%10)
            sum//=10
        return l1