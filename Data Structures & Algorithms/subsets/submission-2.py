class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def bc(index):
            if index == len(nums):
                res.append(subset[::])
                return
            val = nums[index]
            subset.append(val)
            bc(index + 1)

            subset.pop()
            bc(index + 1)
        bc(0)
        return res
            