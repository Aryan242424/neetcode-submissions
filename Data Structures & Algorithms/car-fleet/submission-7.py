class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if there is a car ahead of u then at most 
        # u can add it to your fleet. it starts its own fleet
    
        combined = list(zip(position, speed))
        combined = sorted(combined,reverse=True, key=lambda tup: tup[0])
        stack = []

        for pos, spd in combined:
            time = (target - pos) / spd
            if not stack: 
                stack.append(time)
            else:
                prev_time = stack[-1]
                if prev_time < time:
                    stack.append(time)
            #curr is faster then new fleet

        return len(stack)
            













        