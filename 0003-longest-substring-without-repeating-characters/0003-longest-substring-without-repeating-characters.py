class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = set()
        m, start = 0, 0
        
        for i, num in enumerate(s):
            while num in data:
                data.remove(s[start])
                start += 1
            data.add(s[i])
            m = max(m, i-start+1)
            
        return m