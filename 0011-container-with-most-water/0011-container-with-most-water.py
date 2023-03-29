class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, i = 0, 0
        j = len(height)-1
        
        while i <= j:
            if height[i] < height[j]:
                val = (j-i)*height[i]
                i += 1
            else:
                val = (j-i)*height[j]
                j -= 1
                
            ans = max(ans, val)
            
        return ans