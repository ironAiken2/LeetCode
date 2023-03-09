class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        
        if len(s) == 1:
            return False
        
        open = []
        flag = 0
        
        for i, char in enumerate(s):
            if char == '(' or char == '{' or char == '[':
                open.append(char)
            else:
                if len(open) == 0:
                    return False
                if dic[open[-1]] == char:
                    del open[-1]
                else:
                    flag = 1
                    break
        
        if flag == 0 and len(open) == 0:
            return True
        else:
            return False