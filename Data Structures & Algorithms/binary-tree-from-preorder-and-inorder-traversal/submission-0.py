# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), ValuesView:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_index = {v: i for i, v in enumerate(inorder)}
        self.root_index = 0
        
        def dfs(l, r):
            if l > r: return None

            root_val = preorder[self.root_index]
            self.root_index += 1
            root = TreeNode(root_val)

            mid = in_order_index[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)

