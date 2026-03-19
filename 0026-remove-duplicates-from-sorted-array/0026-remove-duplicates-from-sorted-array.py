class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while(i!=(len(nums)-1)):
            if(nums[i]==nums[j]):
                nums.remove(nums[i])
            else:
                i+=1
                j+=1
        k=len(nums)
        return k