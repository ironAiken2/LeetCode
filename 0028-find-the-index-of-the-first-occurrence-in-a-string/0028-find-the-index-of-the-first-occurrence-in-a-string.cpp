class Solution {
public:
    bool find_needle(string haystack, string needle, int index) {
        for (int i=0;i<needle.size(); i++) {
            if (haystack[index + i] != needle[i]) {
                return false;
            }
        }
        return true;
    };
    int strStr(string haystack, string needle) {
        for (int i=0; i<haystack.size(); i++) {
            if (haystack[i] == needle[0]) {
                if (find_needle(haystack, needle, i) == true) {
                    return i;
                }
            }
        }
        
        return -1;
    };
};