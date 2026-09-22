class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # convert to two sorted arrays
        l = 0 
        r = len(nums) - 1
        while r > l:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # l = m
        search_1 = self.binary_search(nums, l, len(nums) - 1, target)
        if search_1 != -1:
            return search_1
        else:
            return self.binary_search(nums, 0, l - 1, target)

    def binary_search(self, nums: List[int], start: int, end: int, target: int) -> int:
        l = start
        r = end

        while r >= l:
            m = (l + r) // 2

            if nums[m] == target: return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1 


        