class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        temp=''
        while(i<len(s)//2):
            temp=s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=temp
            i+=1
        return s