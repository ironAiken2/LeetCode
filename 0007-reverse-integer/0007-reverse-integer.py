class Solution:
    def reverse(self, x: int) -> int:
        cnt = 1
        
        flag = 1 if x >= 0 else -1
        num = []
        x = abs(x)
        
        while x > 0:
            num.append(x%10)
            x = x//10
            cnt *= 10
        cnt /= 10
        
        i = 0
        ans = 0
        
        while cnt >= 1:
            ans += num[i] * cnt
            cnt /= 10
            i += 1
            
        ans = int(ans) * flag
        
        if ans < -(2**31) or ans > 2**31 - 1:
            return 0
        else:
            return ans
            
            