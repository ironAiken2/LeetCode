class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        cnt = 0
        opp = False
        
        if numRows == 1:
            return s
        
        for ch in s:
            ans[cnt].append(ch)
            
            cnt += 1 if opp == False else -1
            
            if cnt >= numRows:
                opp = True
                cnt -= 2
            if cnt <= -1:
                opp = False
                cnt += 2
        
        result = ''
        
        for l in ans:
            result += ''.join(s for s in l)
            
        return result
        
