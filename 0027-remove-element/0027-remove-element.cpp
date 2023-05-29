class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        nums.erase(remove_if(nums.begin(), nums.end(), [val](auto x) -> bool { return x == as_const(val); }), nums.end());
        
        
        return nums.size();
    };
};