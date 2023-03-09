class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        flag = 0
        s += '0'
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '0' or flag == 1:
                flag = 0
                continue
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    ans += 4 if s[i+1] == 'V' else 9
                    flag = 1
                else:
                    ans += roman[s[i]]
            elif s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    ans += 40 if s[i+1] == 'L' else 90
                    flag = 1
                else:
                    ans += roman[s[i]]
            elif s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    ans += 400 if s[i+1] == 'D' else 900
                    flag = 1
                else:
                    ans += roman[s[i]]
            else:
                ans += roman[s[i]]
                    
        return ans
                    