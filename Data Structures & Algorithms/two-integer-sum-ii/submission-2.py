class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 

        while l < r:
            current_nums = numbers[l] + numbers[r]
            if current_nums > target:
                r -= 1
            elif current_nums < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []