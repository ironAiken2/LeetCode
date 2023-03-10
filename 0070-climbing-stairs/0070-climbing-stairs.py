class Solution(object):
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[-1]
        
        
# n = 1 , 1
# n = 2 , 2
# n = 3 , 3
# n = 4 , 5
# n = 5 , 8
# 점화식 -> n = n-1 + n-2 