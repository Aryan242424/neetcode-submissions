# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def in_order_traversal(root: Optional[TreeNode]) -> List[int]:
            if not root: return []
            return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)
        
        res = in_order_traversal(root)
        return res[k - 1]


        