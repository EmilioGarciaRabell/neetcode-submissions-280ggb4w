class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set(nums)
        return len(newset) != len(nums)