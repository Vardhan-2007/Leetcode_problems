class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minimum=100000
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                current_distance=abs(total-target)
                if current_distance<minimum:
                    minimum=current_distance
                    closest=total
                if total<target:
                    left+=1
                else:
                    right-=1
        return closest