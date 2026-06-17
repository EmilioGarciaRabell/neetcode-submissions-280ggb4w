class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)
        for i in range(n+1):
            # while the top the stack is shorter than the current height pop the top
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                h = heights[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h*w)
            stack.append(i)

        return max_area





