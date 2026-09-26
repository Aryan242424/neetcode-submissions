# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), get_overloads:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, float("-inf"))])
        good_niggas = 0

        while q:
            for i in range(len(q)):
                node, max_so_far = q.popleft()
                if not node: continue
                if node.val >= max_so_far:
                    good_niggas +=1 
                max_so_far = max(max_so_far, node.val)
                q.append((node.left, max_so_far))
                q.append((node.right, max_so_far))
        return good_niggas


        