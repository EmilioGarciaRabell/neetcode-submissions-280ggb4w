class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m * n) - 1

        while l <= r:
            mid = (l+r)//2
            row = mid//n
            col = mid % n
            current_mid = matrix[row][col]

            if current_mid == target:
                return True
            elif current_mid < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


            