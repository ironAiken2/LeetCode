class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, ch):
            if len(ch) == n*2:
                ans.append(ch)
                return
            
            if left < n:
                dfs(left+1, right, ch+'(')
                
            if right < left:
                dfs(left, right+1, ch+')')
                
        ans = []
        dfs(0,0,'')
        return ans