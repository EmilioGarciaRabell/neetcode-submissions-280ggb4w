class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l_max = [0] * n
        r_max = [0] * n

        j = n - 2
        for i in range(1, n):
            l_max[i] = (max(height[i - 1], l_max[i - 1]))
            r_max[j] = (max(height[j+1], r_max[j+1]))

            j -= 1
    
        total_area = 0
        for i in range(len(height)):
            current_area = min(l_max[i], r_max[i]) - height[i]
            if current_area > 0:
                total_area += current_area
            

            
        return total_area
        