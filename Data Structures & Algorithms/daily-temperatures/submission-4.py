class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store nested pairs temp, index
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, index = stack.pop()
                res[index] = i - index
            stack.append([temp, i])

        return res

  
            
