import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        n = len(position)
        sorted_cars = []
        stack = []
        for i in range(n):
            sorted_cars.append((position[i],speed[i]))
        
        sorted_cars.sort()

        for i in range(n - 1 , -1, -1):
            current_car = sorted_cars[i]
            current_car_arrival = (target-current_car[0])/current_car[1]
            if stack:

                past_car_arrival = (target-stack[-1][0])/stack[-1][1]
                if current_car_arrival <= past_car_arrival:
                    continue

            stack.append(current_car)
        return len(stack)
                