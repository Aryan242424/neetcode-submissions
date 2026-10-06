class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        
        def bc(i):
            if i == len(nums):
                return res.append(subset[::])
            
            subset.append(nums[i])
            bc(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bc(i + 1)
        bc(0)
        return res

        