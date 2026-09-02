class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        left_max, right_max = height[l], height[r]

        if not height: return 0

        water = 0
        while (l < r):
            smaller = min(left_max, right_max)

            if (smaller == left_max):
                l += 1
                water = water + max(0, left_max - height[l])
                left_max = max(left_max, height[l])
            else:
                r -= 1
                water = water + max(0, right_max - height[r])
                right_max = max(right_max, height[r])
        return water

