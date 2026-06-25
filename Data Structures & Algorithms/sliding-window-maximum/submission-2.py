class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        maxQueue = []
        l = 0
        for r in range(len(nums)):
            
            maxQueue.append(nums[r])

            # condition for when the window is starting
            if (r - l + 1 ) == k:
                maxElements.append(max(maxQueue))
                l += 1
                maxQueue.pop(0)
            
        return maxElements