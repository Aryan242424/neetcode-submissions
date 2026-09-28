# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        pre_order_traversal = []
        def dfs(root):
            if not root: 
                pre_order_traversal.append("%")
                return

            pre_order_traversal.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "#".join(pre_order_traversal)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.vals = data.split("#")
        self.i = 0

        def dfs():
            if self.vals[self.i] == "%":
                self.i += 1
                return None
  
            root = TreeNode(int(self.vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

    



