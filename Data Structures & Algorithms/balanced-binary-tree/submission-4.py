# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # true if isBalanced
        self.balanced = True

        def height(root: Optional[TreeNode]): #dfs approach
            if not root: return 0
            left_height = height(root.left)
            right_height = height(root.right)
            h = 1 + max(left_height, right_height)

            if abs(left_height - right_height) > 1:
                self.balanced = False
            return h
        height(root)

        return self.balanced

        