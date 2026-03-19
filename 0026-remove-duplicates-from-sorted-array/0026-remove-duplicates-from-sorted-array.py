class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        count=0
        while(i!=(len(nums)-1)):
            if(nums[i]==nums[j]):
                nums.remove(nums[i])
                count+=1
            else:
                i+=1
                j+=1
        k=len(nums)
        for i in range(count):
            nums.append(0)
        return k