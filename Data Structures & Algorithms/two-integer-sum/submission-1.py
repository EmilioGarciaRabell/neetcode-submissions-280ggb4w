class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            left = target - nums[n]
            if left in nums:
                for i in range(n+1,len(nums)):
                    if nums[i] == left:
                        return [n, i]