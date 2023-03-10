# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if not root:
            return []
    
        if root.left != None:
            ans += Solution().inorderTraversal(root.left)
        ans.append(root.val)
        if root.right != None:
            ans += Solution().inorderTraversal(root.right)
        
        return ans