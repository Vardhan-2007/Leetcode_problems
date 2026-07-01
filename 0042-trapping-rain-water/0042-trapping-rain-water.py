class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=height[0]
        rightmax=height[len(height)-1]
        left,right=0,len(height)-1
        count=0
        while left<right:
            if leftmax<rightmax:
                left+=1
                if height[left]<leftmax:
                    count+=leftmax-height[left]
                else:
                    leftmax=height[left]
            else:
                right-=1
                if height[right]<rightmax:
                    count+=rightmax-height[right]
                else:
                    rightmax=height[right]
        return count