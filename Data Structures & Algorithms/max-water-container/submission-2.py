class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) -1 

        max_content = 0
        while l < r:
            min_val = min(heights[l], heights[r])
            current_content = min_val * (r-l)

            max_content = max(max_content, current_content)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_content