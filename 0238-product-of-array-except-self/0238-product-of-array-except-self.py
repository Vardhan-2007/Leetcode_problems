class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i]=nums[i]
                postfix[len(nums)-1]=nums[len(nums)-1]
            else:
                prefix[i]=nums[i]*prefix[i-1]
                postfix[len(nums)-i-1]=nums[len(nums)-i-1]*postfix[len(nums)-i]
        for i in range(len(nums)):
            if i==0:
                res[i]=postfix[i+1]
            elif i==len(nums)-1:
                res[i]=prefix[i-1]
            else:
                res[i]=prefix[i-1]*postfix[i+1]
        return res