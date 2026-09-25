# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        return self.height_and_diameter(root)[1]
        
    def height_and_diameter(self, root: Optional[TreeNode]) -> tuple(int, int):
        if not root: return (0, 0)
        left_height, left_diameter = self.height_and_diameter(root.left)
        right_height, right_diameter = self.height_and_diameter(root.right)
        diameter = max(left_diameter, right_diameter, left_height + right_height)
        height = 1 + max(left_height, right_height)

        return (height, diameter)


        