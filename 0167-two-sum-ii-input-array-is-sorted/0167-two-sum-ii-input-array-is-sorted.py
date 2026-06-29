class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            sum1=numbers[left]+numbers[right]
            if sum1==target:
                return left+1,right+1
            elif sum1<target:
                left+=1
            else:
                right-=1
            