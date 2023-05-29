#include <cmath>

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        long int c = x, flag = 0;
        
        while (c > 0) {
            flag *= 10;
            flag += c % 10;
            c /= 10;
        }
                
        if (x == flag) {
            return true;
        }
        
        return false;
    }
};