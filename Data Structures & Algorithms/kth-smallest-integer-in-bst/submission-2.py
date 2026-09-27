# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        def in_order_traversal(root: Optional[TreeNode]) -> None:
            if not root: return
            in_order_traversal(root.left)     
            self.res.append(root.val)
            in_order_traversal(root.right)
        
        in_order_traversal(root)
        return self.res[k - 1]


        