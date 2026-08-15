class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(list)
        for n in nums:
            count[n]=1+count.get(n,0)
        res=[]
        for n in count:
            if count[n]>(len(nums)/3):
                res.append(n)
        return res