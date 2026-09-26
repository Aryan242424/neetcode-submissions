# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
         # what makes an invalid bst guaranteed - if right or left are invalid

        
        def dfs_helper(root: Optional[TreeNode]) -> tuple[bool, int, int]:
            if not root: return (True, float("-inf"), float("inf"))
            r_valid, r_biggest, r_smallest = dfs_helper(root.right)
            l_valid, l_biggest, l_smallest = dfs_helper(root.left)

            biggest = max(root.val, r_biggest)
            smallest = min(root.val, l_smallest)
            valid =  (r_valid and l_valid) and (r_smallest > root.val) and (root.val > l_biggest)

            return (valid, biggest, smallest)

        return dfs_helper(root)[0]

            


    



        