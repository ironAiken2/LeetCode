# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []
        
        if root.left:
            left += Solution().levelOrder1(root.left)
        if root.right:
            right += Solution().levelOrder2(root.right)
                
        if left == right:
            return True
        else:
            return False
        
    def levelOrder1(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        
        ans.append(root.val)
        
        if root.left:
            ans += Solution().levelOrder1(root.left)
        else:
            ans += ' '
        if root.right:
            ans += Solution().levelOrder1(root.right)
        else:
            ans += ' '
            
        return ans
    
    def levelOrder2(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        
        ans.append(root.val)
        
        if root.right:
            ans += Solution().levelOrder2(root.right)
        else:
            ans += ' '
        if root.left:
            ans += Solution().levelOrder2(root.left)
        else:
            ans += ' '
            
        return ans