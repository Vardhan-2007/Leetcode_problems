class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        while left < len(nums):
            if nums[left] == 0:
                left += 1
                continue
            right = left + 1
            while right < len(nums) and nums[right] != 0:
                right += 1
            if right == len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        while left < len(nums):
            if nums[left] == 1:
                left += 1
                continue
            right = left + 1
            while right < len(nums) and nums[right] != 1:
                right += 1
            if right == len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        while left < len(nums):
            if nums[left] == 2:
                left += 1
                continue
            right = left + 1
            while right < len(nums) and nums[right] != 2:
                right += 1
            if right == len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1