class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublst in matrix:
            l = 0
            r = len(sublst) - 1
            while r >= l:
                m = l + (r - l) // 2

                if sublst[m] == target:
                    return True
                elif sublst[m] > target:
                    r = m - 1
                else:
                    l = m + 1

        return False
        