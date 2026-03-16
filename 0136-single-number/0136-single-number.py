class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        j=0
        for i in nums:
            j=j^i
        return j