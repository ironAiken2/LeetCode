# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cnt1 = 1
        cnt2 = 1
        
        if root.left:
            cnt1 += Solution().maxDepth(root.left)
        if root.right:
            cnt2 += Solution().maxDepth(root.right)
            
        if cnt1 > cnt2:
            return cnt1
        else:
            return cnt2