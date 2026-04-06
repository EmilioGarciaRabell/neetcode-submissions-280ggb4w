class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct_elements_count = {}
        most_frequent = [[] for _ in range(len(nums) + 1)]
    
        result = []
        for num in nums:
            if num not in distinct_elements_count:
                distinct_elements_count[num] = 1
            else:
                distinct_elements_count[num] += 1
            
        for key, value in distinct_elements_count.items():
            most_frequent[value].append(key)

        for i in range(len(most_frequent) - 1, 0, -1):
            for n in most_frequent[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result
