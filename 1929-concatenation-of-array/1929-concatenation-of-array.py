class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        count=0
        i=0
        while i<len(nums):
            ans.append(nums[i])
            i+=1
            if i==len(nums):
                count+=1
                i=0
            if count==2:
                break
        return ans