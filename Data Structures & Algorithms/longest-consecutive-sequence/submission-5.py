class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_count = set()

        for num in nums:
            nums_count.add(num)

        possible_start = set()

        for num in nums:
            if num - 1 not in nums_count:
                possible_start.add(num)
        
       
        max_len = 0
        for num in nums:
            current_sequence = 0
            if num in possible_start:
                
                current_num = num
                while current_num in nums_count:
                    current_num += 1
                    current_sequence += 1
                
                max_len = max(current_sequence, max_len)
                
        return max_len

        