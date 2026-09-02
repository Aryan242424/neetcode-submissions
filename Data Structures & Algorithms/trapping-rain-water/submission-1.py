class Solution:
    def trap(self, height: List[int]) -> int:
        max_right_so_far, max_left_so_far = 0, 0
        max_left_lst = [0] * len(height)
        max_right_lst = [0] * len(height)

        for i in range(len(height)):
            j = -i - 1  # python negative indexing
            curr_left, curr_right = height[i], height[j]

            max_left_lst[i] = max_left_so_far
            max_right_lst[j] = max_right_so_far

            max_left_so_far = max(curr_left, max_left_so_far)
            max_right_so_far = max(curr_right,          max_right_so_far)
        
        #
        acc = 0
        for i in range(len(height)):
            min_height = min(max_left_lst[i], max_right_lst[i])

            acc += max(min_height - height[i], 0)
        return acc
