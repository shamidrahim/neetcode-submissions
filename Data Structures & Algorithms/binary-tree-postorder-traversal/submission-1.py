# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = [False]
        stack = [root]
        res = []
        while stack:
            visited, cur = visit.pop(), stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res
        
        