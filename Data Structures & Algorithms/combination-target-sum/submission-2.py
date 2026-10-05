class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(index, total):
            if index == len(nums) or total > target:
                return
            if total == target:
                res.append(combination[::])
                return
            
            combination.append(nums[index])
            dfs(index, total + nums[index])

            combination.pop()
            dfs(index + 1, total)
        
        dfs(0, 0)
        return res


        