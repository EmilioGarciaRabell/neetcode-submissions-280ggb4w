class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("infinity")

        while r >= l:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break

            m = (l + r)//2
            minVal = min(nums[m], minVal)
            if nums[m] >= nums[l]:
                    l = m + 1
            else:
                r = m - 1
                 
        return minVal