class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0, i;
        for (i = s.size()-1; i >= 0; i--) {
            if (s[i] != ' ') {
                break;
            }
        }
        for (i; i >= 0; i--) {
            if (s[i] == ' ') {
                return cnt;
            }
            cnt += 1;
        }
        
        return cnt;
    }
};