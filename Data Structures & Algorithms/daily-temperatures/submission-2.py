class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        
        for i in range(n):
            # check if current temp is greater 
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                past_indx = stack.pop()
                result[past_indx] = i - past_indx

            stack.append(i)
        return result
