class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r=(len(nums)*(len(nums)+1))//2
        sum=0
        for i in nums:
            sum+=i
        return r-sum