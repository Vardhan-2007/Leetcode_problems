class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if(target>nums[i]):
                pass
            elif(target<nums[i]):
                return i
            else:
                return i
        return len(nums)