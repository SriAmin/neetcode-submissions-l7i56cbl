class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 1:
            return 1
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for car in cars:
            pos, spd = car
            x = (target - pos) / spd
            # stack.append(x)
            if len(stack) < 1 or x > stack[-1]:
                stack.append(x)
        return len(stack)

            
