class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        for data in Counter(s):
            dic[data] = 0
        
        start = 0
        end = 0
        ans = 0
        
        while end < len(s):
            if dic[s[end]] == 0:
                dic[s[end]] += 1
                end += 1
            else:
                dic[s[start]] -= 1
                start += 1
                
            ans = max(ans, end - start)
                
        return ans