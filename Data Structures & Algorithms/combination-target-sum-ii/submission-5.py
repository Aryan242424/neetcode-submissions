class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                res.append(combo[::])
                return 
            if index == len(candidates) or total > target:
                return
            
            combo.append(candidates[index])
            dfs(index + 1, total + candidates[index])
            combo.pop()
            ## branch 2
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, total)

        dfs(0, 0)
        return res        