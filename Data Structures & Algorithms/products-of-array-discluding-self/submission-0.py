class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = []
        for i in range(0,len(nums)):
            
            prefix = nums[:i]
            suffix = nums[i+1:]

            result_at_i = 1
            for j in prefix:
                result_at_i *= j
            for j in suffix:
                result_at_i *= j
            results.append(result_at_i)
        return results