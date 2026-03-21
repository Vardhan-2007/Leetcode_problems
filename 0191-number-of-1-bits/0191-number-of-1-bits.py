class Solution:
    def hammingWeight(self, n: int) -> int:
        if(n//2==0):
            return 1
        return (n%2)+self.hammingWeight(n//2)