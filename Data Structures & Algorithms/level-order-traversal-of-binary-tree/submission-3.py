# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [[root.val]]
        l1, l2 = self.levelOrder(root.left), self.levelOrder(root.right)
        smaller = l1 if len(l1) < len(l2) else l2

        for i in range(len(smaller)):
            combined = l1[i] + l2[i]
            res.append(combined)
        
        if smaller == l1:
            res.extend(l2[len(l1) ::])
        else:
            res.extend(l1[len(l2)::])
        return res