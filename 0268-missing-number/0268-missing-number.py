class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum+=i
        return ((len(nums)*(len(nums)+1))//2)-sum