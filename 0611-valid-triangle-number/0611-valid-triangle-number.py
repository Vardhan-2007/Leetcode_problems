class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        valid=0
        i=len(nums)-1
        while i>1:
            left,right=0,i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    valid+=right-left
                    right-=1
                else:
                    left+=1
            i-=1
        return valid