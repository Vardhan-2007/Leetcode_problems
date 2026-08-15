class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(list)
        for n in nums:
            count[n]=1+count.get(n,0)
        res=[]
        appear=len(nums)/3
        for n in count:
            if count[n]>(appear):
                res.append(n)
        return res