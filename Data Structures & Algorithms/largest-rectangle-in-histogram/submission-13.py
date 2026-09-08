class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][0]: 
                stack.append((h, i))
                continue
            
            # else h > stack[-1][0]
            new_index = i
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                max_area = max(max_area, (i - index) * height)
                new_index = index
            stack.append((h, new_index))
        
        for h, i in stack:
            max_area = max((len(heights) - i) * h, max_area)

        return max_area
                




            




        