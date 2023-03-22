class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        if numRows == 1:
            return ans
        
        ans.append([1,1])
        
        for i in range(2,numRows):
            ans.append([1])
                        
            for j in range(len(ans[i-1])-1):
                ans[i].append(ans[i-1][j] + ans[i-1][j+1])
                
            ans[i].append(1)
            
        return ans