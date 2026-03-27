class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        if len(nums)!=len(nums1):
            return True
        return False