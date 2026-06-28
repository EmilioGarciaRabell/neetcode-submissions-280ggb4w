class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = (m * n) - 1

        while l <= r:
            midIdx = (r + l)//2
            mid = matrix[midIdx // n][midIdx % n]

            if mid > target:
                r = midIdx - 1
            elif mid < target:
                l = midIdx + 1
            elif mid == target:
                return True
        return False