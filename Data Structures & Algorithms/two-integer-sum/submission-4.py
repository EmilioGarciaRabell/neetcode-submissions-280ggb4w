class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       

        new_list = []

        for i, num in enumerate(nums):
            new_list.append([num, i])

        new_list.sort();
        left = 0;
        right = len(nums) - 1
        while left < right:
            current_sum = new_list[left][0] + new_list[right][0]

            if current_sum == target:
                return [min(new_list[left][1], new_list[right][1]), max(new_list[left][1], new_list[right][1])]
            elif current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
        
        return []