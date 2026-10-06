class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])

        curr = nums[0]
        for p in perms:
            for i in range(len(p) + 1):
                copy = p[::] # make copy
                copy.insert(i, curr)
                res.append(copy)

        return res
        