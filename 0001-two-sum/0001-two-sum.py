class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if (target - i) in nums[(nums.index(i)) + 1:]:
                return [nums.index(i), nums.index(target - i, nums.index(i) + 1)]