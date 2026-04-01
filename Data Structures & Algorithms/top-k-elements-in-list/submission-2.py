class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for n in nums:
            result[n] = 1 + result.get(n, 0)

        arr = []

        for key, value in result.items():
            arr.append([value, key])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res