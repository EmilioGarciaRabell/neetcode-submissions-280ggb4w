class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums:
            current_count = 0
            if num - 1 not in nums:
                current_count += 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_count += 1
                max_count = max(current_count, max_count)

        return max_count

        